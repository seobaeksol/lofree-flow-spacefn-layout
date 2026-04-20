#!/usr/bin/env python3

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


KEYMAP_WORDS = 75 * 6
KNOWN_V14_KEYMAP_BASE = 0x0800E574
LOFREE_VENDOR_PRODUCT_ID = (0x388D << 16) | 0x0001

# Unique factory-default signature for the v14 OE928 firmware. This is the
# start of layer 0 in row-major matrix order.
KEYMAP_SIGNATURE = bytes.fromhex(
    "29 00 1E 00 1F 00 20 00 21 00 22 00 23 00 24 00"
    " 25 00 26 00 27 00 2D 00 2E 00 2A 00 4C 00"
)

# Standard HID/basic QMK keycodes used by the current layouts in this repo.
BASIC_KEYCODES = {
    "KC_NO": 0x0000,
    "KC_TRNS": 0x0001,
    "KC_A": 0x0004,
    "KC_B": 0x0005,
    "KC_C": 0x0006,
    "KC_D": 0x0007,
    "KC_E": 0x0008,
    "KC_F": 0x0009,
    "KC_G": 0x000A,
    "KC_H": 0x000B,
    "KC_I": 0x000C,
    "KC_J": 0x000D,
    "KC_K": 0x000E,
    "KC_L": 0x000F,
    "KC_M": 0x0010,
    "KC_N": 0x0011,
    "KC_O": 0x0012,
    "KC_P": 0x0013,
    "KC_Q": 0x0014,
    "KC_R": 0x0015,
    "KC_S": 0x0016,
    "KC_T": 0x0017,
    "KC_U": 0x0018,
    "KC_V": 0x0019,
    "KC_W": 0x001A,
    "KC_X": 0x001B,
    "KC_Y": 0x001C,
    "KC_Z": 0x001D,
    "KC_1": 0x001E,
    "KC_2": 0x001F,
    "KC_3": 0x0020,
    "KC_4": 0x0021,
    "KC_5": 0x0022,
    "KC_6": 0x0023,
    "KC_7": 0x0024,
    "KC_8": 0x0025,
    "KC_9": 0x0026,
    "KC_0": 0x0027,
    "KC_ENT": 0x0028,
    "KC_ESC": 0x0029,
    "KC_BSPC": 0x002A,
    "KC_TAB": 0x002B,
    "KC_SPC": 0x002C,
    "KC_MINS": 0x002D,
    "KC_EQL": 0x002E,
    "KC_LBRC": 0x002F,
    "KC_RBRC": 0x0030,
    "KC_BSLS": 0x0031,
    "KC_SCLN": 0x0033,
    "KC_QUOT": 0x0034,
    "KC_GRV": 0x0035,
    "KC_COMM": 0x0036,
    "KC_DOT": 0x0037,
    "KC_SLSH": 0x0038,
    "KC_CAPS": 0x0039,
    "KC_F1": 0x003A,
    "KC_F2": 0x003B,
    "KC_F3": 0x003C,
    "KC_F4": 0x003D,
    "KC_F5": 0x003E,
    "KC_F6": 0x003F,
    "KC_F7": 0x0040,
    "KC_F8": 0x0041,
    "KC_F9": 0x0042,
    "KC_F10": 0x0043,
    "KC_F11": 0x0044,
    "KC_F12": 0x0045,
    "KC_PGUP": 0x004B,
    "KC_DEL": 0x004C,
    "KC_END": 0x004D,
    "KC_PGDN": 0x004E,
    "KC_RGHT": 0x004F,
    "KC_LEFT": 0x0050,
    "KC_DOWN": 0x0051,
    "KC_UP": 0x0052,
    "KC_HOME": 0x004A,
    "KC_APP": 0x0065,
    "KC_WWW_SEARCH": 0x00B4,
    "KC_BRIU": 0x00BD,
    "KC_BRID": 0x00BE,
    "KC_MUTE": 0x00A8,
    "KC_VOLU": 0x00A9,
    "KC_VOLD": 0x00AA,
    "KC_MNXT": 0x00AB,
    "KC_MPRV": 0x00AC,
    "KC_MPLY": 0x00AE,
    "KC_LCTL": 0x00E0,
    "KC_LSFT": 0x00E1,
    "KC_LALT": 0x00E2,
    "KC_LGUI": 0x00E3,
    "KC_RCTL": 0x00E4,
    "KC_RSFT": 0x00E5,
    "KC_RALT": 0x00E6,
    "KC_RGUI": 0x00E7,
}

SPECIAL_KEYCODES = {
    "BL_DEC": 0x7803,
    "BL_INC": 0x7804,
    "RESET": 0x7C00,
    "QK_CLEAR_EEPROM": 0x7C03,
    "MAGIC_TOGGLE_NKRO": 0x7013,
}

# In this firmware family, the factory-default keymap does not store the QMK
# connection keycodes directly. Instead it uses keyboard-specific QK_KB slots.
FIRMWARE_BT_MAP = {
    "0x7793": 0x7E01,  # Bluetooth profile 1
    "0x7794": 0x7E02,  # Bluetooth profile 2
    "0x7795": 0x7E03,  # Bluetooth profile 3
    "0x7785": 0x7E04,  # 2.4 GHz
}

VALUE_TO_BASIC = {value: key for key, value in BASIC_KEYCODES.items()}
VALUE_TO_SPECIAL = {value: key for key, value in SPECIAL_KEYCODES.items()}
VALUE_TO_BT = {value: key for key, value in FIRMWARE_BT_MAP.items()}


@dataclass
class Record:
    rectype: int
    address: int
    data: bytearray
    raw: str


def parse_hex(path: Path) -> list[Record]:
    records: list[Record] = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        if not line.startswith(":"):
            raise ValueError(f"invalid Intel HEX line: {line!r}")
        count = int(line[1:3], 16)
        address = int(line[3:7], 16)
        rectype = int(line[7:9], 16)
        data = bytearray.fromhex(line[9 : 9 + count * 2])
        checksum = int(line[9 + count * 2 : 11 + count * 2], 16)
        total = count + (address >> 8) + (address & 0xFF) + rectype + sum(data) + checksum
        if (total & 0xFF) != 0:
            raise ValueError(f"checksum mismatch: {line}")
        records.append(Record(rectype=rectype, address=address, data=data, raw=line))
    return records


def build_memory(records: list[Record]) -> tuple[dict[int, int], int, int]:
    memory: dict[int, int] = {}
    base = 0
    minimum = None
    maximum = 0
    for record in records:
        if record.rectype == 0x00:
            absolute = base + record.address
            for i, byte in enumerate(record.data):
                memory[absolute + i] = byte
            if minimum is None or absolute < minimum:
                minimum = absolute
            maximum = max(maximum, absolute + len(record.data))
        elif record.rectype == 0x04:
            base = int.from_bytes(record.data, "big") << 16
        elif record.rectype == 0x01:
            break
    if minimum is None:
        raise ValueError("no data records found")
    return memory, minimum, maximum


def encode_token(token: str) -> int:
    if token in BASIC_KEYCODES:
        return BASIC_KEYCODES[token]
    if token in SPECIAL_KEYCODES:
        return SPECIAL_KEYCODES[token]
    if token in FIRMWARE_BT_MAP:
        return FIRMWARE_BT_MAP[token]

    custom_match = re.fullmatch(r"CUSTOM\((\d+)\)", token)
    if custom_match:
        return 0x7E04 + int(custom_match.group(1))

    mo_match = re.fullmatch(r"MO\((\d+)\)", token)
    if mo_match:
        return 0x5220 + int(mo_match.group(1))

    to_match = re.fullmatch(r"TO\((\d+)\)", token)
    if to_match:
        return 0x5200 + int(to_match.group(1))

    lt_match = re.fullmatch(r"LT\((\d+),([A-Z0-9_]+)\)", token)
    if lt_match:
        layer = int(lt_match.group(1))
        tap = lt_match.group(2)
        if tap not in BASIC_KEYCODES or BASIC_KEYCODES[tap] > 0xFF:
            raise ValueError(f"LT tap key must be a basic keycode: {token}")
        return 0x4000 | ((layer & 0x0F) << 8) | BASIC_KEYCODES[tap]

    raise ValueError(f"unsupported key token: {token}")


def locate_keymap_base(memory: dict[int, int], minimum: int, maximum: int) -> int:
    blob = bytes(memory.get(addr, 0xFF) for addr in range(minimum, maximum))
    index = blob.find(KEYMAP_SIGNATURE)
    if index == -1:
        candidate = KNOWN_V14_KEYMAP_BASE
        end = candidate + KEYMAP_WORDS * 2
        if all(addr in memory for addr in range(candidate, end)):
            return candidate
        raise ValueError("could not locate OE928 v14 default keymap block")
    return minimum + index


def read_keymap_words(memory: dict[int, int], base: int) -> list[int]:
    words = []
    for offset in range(0, KEYMAP_WORDS * 2, 2):
        lo = memory[base + offset]
        hi = memory[base + offset + 1]
        words.append(lo | (hi << 8))
    return words


def decode_word(word: int) -> str:
    if word in VALUE_TO_BT:
        return VALUE_TO_BT[word]
    if word in VALUE_TO_SPECIAL:
        return VALUE_TO_SPECIAL[word]
    if word in VALUE_TO_BASIC:
        return VALUE_TO_BASIC[word]
    if 0x5200 <= word <= 0x521F:
        return f"TO({word - 0x5200})"
    if 0x5220 <= word <= 0x523F:
        return f"MO({word - 0x5220})"
    if 0x4000 <= word <= 0x4FFF:
        layer = (word >> 8) & 0x0F
        tap = word & 0x00FF
        tap_name = VALUE_TO_BASIC.get(tap, f"0x{tap:02X}")
        return f"LT({layer},{tap_name})"
    if 0x7E04 <= word <= 0x7E23:
        return f"CUSTOM({word - 0x7E04})"
    return f"0x{word:04X}"


def load_layout_words(path: Path) -> list[int]:
    obj = json.loads(path.read_text())
    layers = obj.get("layers")
    if not isinstance(layers, list) or len(layers) != 6:
        raise ValueError("expected a VIA save file with 6 layers")
    words: list[int] = []
    for layer_index, layer in enumerate(layers):
        if not isinstance(layer, list) or len(layer) != 75:
            raise ValueError(f"layer {layer_index} must contain 75 keys")
        for token in layer:
            if not isinstance(token, str):
                raise ValueError(f"non-string token in layer {layer_index}: {token!r}")
            words.append(encode_token(token))
    return words


def words_to_layout(words: list[int]) -> dict:
    layers = []
    for layer in range(6):
        start = layer * 75
        end = start + 75
        layers.append([decode_word(word) for word in words[start:end]])
    return {
        "name": "Extracted from references/oe928_v14_vendor.hex",
        "vendorProductId": LOFREE_VENDOR_PRODUCT_ID,
        "layers": layers,
        "macros": ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    }


def patch_records(records: list[Record], patch_bytes: dict[int, int]) -> list[str]:
    output: list[str] = []
    base = 0
    for record in records:
        if record.rectype == 0x00:
            absolute = base + record.address
            for i in range(len(record.data)):
                addr = absolute + i
                if addr in patch_bytes:
                    record.data[i] = patch_bytes[addr]
        elif record.rectype == 0x04:
            base = int.from_bytes(record.data, "big") << 16

        count = len(record.data)
        total = count + (record.address >> 8) + (record.address & 0xFF) + record.rectype + sum(record.data)
        checksum = (-total) & 0xFF
        output.append(f":{count:02X}{record.address:04X}{record.rectype:02X}{record.data.hex().upper()}{checksum:02X}")
    return output


def print_words(words: list[int], decode: bool = False) -> None:
    for layer in range(6):
        print(f"layer {layer}")
        for row in range(5):
            row_words = words[layer * 75 + row * 15 : layer * 75 + (row + 1) * 15]
            if decode:
                print(" ", row, " | ".join(decode_word(word) for word in row_words))
            else:
                print(" ", row, " ".join(f"{word:04X}" for word in row_words))


def cmd_dump(args: argparse.Namespace) -> int:
    records = parse_hex(Path(args.input))
    memory, minimum, maximum = build_memory(records)
    base = locate_keymap_base(memory, minimum, maximum)
    print(f"keymap_base=0x{base:08X}")
    print_words(read_keymap_words(memory, base), decode=args.decode)
    return 0


def cmd_extract(args: argparse.Namespace) -> int:
    input_path = Path(args.input)
    output_path = Path(args.output)
    records = parse_hex(input_path)
    memory, minimum, maximum = build_memory(records)
    base = locate_keymap_base(memory, minimum, maximum)
    words = read_keymap_words(memory, base)
    layout = words_to_layout(words)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(layout, indent=2) + "\n")
    print(f"extracted keymap_base=0x{base:08X}")
    print(f"output={output_path}")
    return 0


def cmd_patch(args: argparse.Namespace) -> int:
    input_path = Path(args.input)
    layout_path = Path(args.layout)
    output_path = Path(args.output)

    records = parse_hex(input_path)
    memory, minimum, maximum = build_memory(records)
    base = locate_keymap_base(memory, minimum, maximum)
    old_words = read_keymap_words(memory, base)
    new_words = load_layout_words(layout_path)

    patch_bytes: dict[int, int] = {}
    for index, word in enumerate(new_words):
        absolute = base + index * 2
        patch_bytes[absolute] = word & 0xFF
        patch_bytes[absolute + 1] = (word >> 8) & 0xFF

    output_lines = patch_records(records, patch_bytes)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(output_lines) + "\n")

    changed = sum(1 for old, new in zip(old_words, new_words) if old != new)
    print(f"patched {changed} / {KEYMAP_WORDS} keymap entries")
    print(f"keymap_base=0x{base:08X}")
    print(f"output={output_path}")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Inspect or patch the default keymap block inside OE928 Flow 2 v14 firmware."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    dump_parser = subparsers.add_parser("dump", help="Dump the embedded 6-layer default keymap")
    dump_parser.add_argument("input", help="Path to the vendor Intel HEX firmware")
    dump_parser.add_argument("--decode", action="store_true", help="Show decoded QMK/VIA-style tokens")
    dump_parser.set_defaults(func=cmd_dump)

    extract_parser = subparsers.add_parser(
        "extract", help="Extract the embedded 6-layer default keymap as a VIA save JSON"
    )
    extract_parser.add_argument("input", help="Path to the vendor Intel HEX firmware")
    extract_parser.add_argument("output", help="Path for the extracted VIA save JSON")
    extract_parser.set_defaults(func=cmd_extract)

    patch_parser = subparsers.add_parser("patch", help="Patch the embedded default keymap from a VIA layout JSON")
    patch_parser.add_argument("input", help="Path to the vendor Intel HEX firmware")
    patch_parser.add_argument("layout", help="Path to a 6-layer VIA save JSON")
    patch_parser.add_argument("output", help="Path for the patched Intel HEX")
    patch_parser.set_defaults(func=cmd_patch)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
