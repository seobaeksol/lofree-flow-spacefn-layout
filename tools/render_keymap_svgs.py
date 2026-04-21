#!/usr/bin/env python3

import html
import json
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFINITION_PATH = ROOT / "references" / "oe928_via_definition_20251114.json"
LAYOUT_PATH = ROOT / "layouts" / "spacefn" / "flow2_lofree_spacefn.layout.json"
OUT_DIR = ROOT / "docs" / "images" / "keymaps"
PNG_OUT_DIR = ROOT / "docs" / "images" / "png"

UNIT = 86
KEY_H = 72
GAP = 8
BOARD_PAD_X = 42
BOARD_PAD_Y = 44
CANVAS_W = 1560
CANVAS_H = 560
KEY_Y_OFFSET = 88

LAYER_META = [
    {"index": 0, "name": "Layer 0", "title": "Mac Base", "accent": "#3f6d88"},
    {"index": 1, "name": "Layer 1", "title": "Mac SpaceFn", "accent": "#2f8a7f"},
    {"index": 2, "name": "Layer 2", "title": "Windows Base", "accent": "#8a6a3e"},
    {"index": 3, "name": "Layer 3", "title": "Windows SpaceFn", "accent": "#c45a2c"},
    {"index": 4, "name": "Layer 4", "title": "Special", "accent": "#6d7b86"},
    {"index": 5, "name": "Layer 5", "title": "Deep Special", "accent": "#8c6277"},
]

MAC_GUI_LABELS = {
    "KC_LGUI": "Cmd",
    "KC_RGUI": "Cmd",
    "KC_LALT": "Opt",
    "KC_RALT": "Opt",
}

WIN_GUI_LABELS = {
    "KC_LGUI": "Win",
    "KC_RGUI": "Win",
    "KC_LALT": "Alt",
    "KC_RALT": "Alt",
    "KC_APP": "Menu",
}

TOKEN_LABELS = {
    "KC_GRV": "~",
    "KC_1": "1",
    "KC_2": "2",
    "KC_3": "3",
    "KC_4": "4",
    "KC_5": "5",
    "KC_6": "6",
    "KC_7": "7",
    "KC_8": "8",
    "KC_9": "9",
    "KC_0": "0",
    "KC_MINS": "-",
    "KC_EQL": "=",
    "KC_BSPC": "Backspace",
    "KC_DEL": "Delete",
    "KC_ESC": "Esc",
    "KC_TAB": "Tab",
    "KC_Q": "Q",
    "KC_W": "W",
    "KC_E": "E",
    "KC_R": "R",
    "KC_T": "T",
    "KC_Y": "Y",
    "KC_U": "U",
    "KC_I": "I",
    "KC_O": "O",
    "KC_P": "P",
    "KC_LBRC": "[",
    "KC_RBRC": "]",
    "KC_BSLS": "\\",
    "KC_CAPS": "Caps",
    "KC_A": "A",
    "KC_S": "S",
    "KC_D": "D",
    "KC_F": "F",
    "KC_G": "G",
    "KC_H": "H",
    "KC_J": "J",
    "KC_K": "K",
    "KC_L": "L",
    "KC_SCLN": ";",
    "KC_QUOT": "'",
    "KC_ENT": "Enter",
    "KC_HOME": "Home",
    "KC_LSFT": "Shift",
    "KC_Z": "Z",
    "KC_X": "X",
    "KC_C": "C",
    "KC_V": "V",
    "KC_B": "B",
    "KC_N": "N",
    "KC_M": "M",
    "KC_COMM": ",",
    "KC_DOT": ".",
    "KC_SLSH": "/",
    "KC_RSFT": "Shift",
    "KC_UP": "Up",
    "KC_END": "End",
    "KC_LCTL": "Ctrl",
    "KC_RCTL": "Ctrl",
    "KC_SPC": "Space",
    "KC_LEFT": "Left",
    "KC_DOWN": "Down",
    "KC_RGHT": "Right",
    "KC_F1": "F1",
    "KC_F2": "F2",
    "KC_F3": "F3",
    "KC_F4": "F4",
    "KC_F5": "F5",
    "KC_F6": "F6",
    "KC_F7": "F7",
    "KC_F8": "F8",
    "KC_F9": "F9",
    "KC_F10": "F10",
    "KC_F11": "F11",
    "KC_F12": "F12",
    "KC_BRID": "Bri-",
    "KC_BRIU": "Bri+",
    "KC_WWW_SEARCH": "Search",
    "BL_DEC": "BL-",
    "BL_INC": "BL+",
    "KC_MPRV": "Prev",
    "KC_MPLY": "Play",
    "KC_MNXT": "Next",
    "KC_MUTE": "Mute",
    "KC_VOLD": "Vol-",
    "KC_VOLU": "Vol+",
    "KC_PGUP": "PgUp",
    "KC_PGDN": "PgDn",
    "MAGIC_TOGGLE_NKRO": "NKRO",
    "RESET": "Reset",
    "QK_CLEAR_EEPROM": "Clear\nEEPROM",
    "KC_TRNS": "TRNS",
    "KC_NO": "NO",
    "0x7793": "BT1",
    "0x7794": "BT2",
    "0x7795": "BT3",
    "0x7785": "2.4G",
    "0x7E00": "Custom\n0",
}

CUSTOM_LABELS = {
    "CUSTOM(7)": "Display",
    "CUSTOM(8)": "Lock?",
    "CUSTOM(10)": "Ambi-",
    "CUSTOM(11)": "Custom\n11?",
    "CUSTOM(13)": "Touch",
    "CUSTOM(14)": "Ambi+",
    "CUSTOM(16)": "Fn/#",
}


def parse_layout_geometry(definition):
    rows = definition["layouts"]["keymap"]
    keys = []
    for row_index, row in enumerate(rows):
        x_units = 0.0
        current_w = 1.0
        for item in row:
            if isinstance(item, dict):
                if "w" in item:
                    current_w = float(item["w"])
                if "x" in item:
                    x_units += float(item["x"])
                continue
            matrix_row, matrix_col = [int(v) for v in item.split(",")]
            keys.append(
                {
                    "row": matrix_row,
                    "col": matrix_col,
                    "x": BOARD_PAD_X + x_units * UNIT,
                    "y": KEY_Y_OFFSET + row_index * UNIT,
                    "w": current_w * UNIT - GAP,
                    "h": KEY_H,
                }
            )
            x_units += current_w
            current_w = 1.0
    return keys


def format_label(token, layer_index):
    if layer_index in (0, 1):
        if token in MAC_GUI_LABELS:
            return MAC_GUI_LABELS[token]
    if layer_index in (2, 3):
        if token in WIN_GUI_LABELS:
            return WIN_GUI_LABELS[token]

    if token in TOKEN_LABELS:
        return TOKEN_LABELS[token]
    if token in CUSTOM_LABELS:
        return CUSTOM_LABELS[token]
    if token.startswith("LT(") and token.endswith(")"):
        return "SpaceFn"
    if token.startswith("MO(") and token.endswith(")"):
        return f"L{token[3:-1]}"
    if token.startswith("TO(") and token.endswith(")"):
        target = token[3:-1]
        if target == "0":
            return "Mac"
        if target == "2":
            return "Win"
        return f"To {target}"
    if token.startswith("KC_"):
        return token[3:]
    return token


def key_style(token, layer_index, accent):
    if token == "KC_TRNS":
        return {
            "fill": "#eef1f4",
            "stroke": "#d8dde2",
            "text": "#8e99a3",
            "subtle": True,
        }
    if token == "KC_NO":
        return {
            "fill": "#e5e8eb",
            "stroke": "#d4d9df",
            "text": "#8f969d",
            "subtle": True,
        }
    if layer_index in (1, 3, 4):
        return {
            "fill": "#ffffff",
            "stroke": accent,
            "text": "#24323d",
            "subtle": False,
        }
    return {
        "fill": "#ffffff",
        "stroke": "#d5dbe0",
        "text": "#26343d",
        "subtle": False,
    }


def split_label(label):
    if "\n" in label:
        return label.split("\n")
    if len(label) <= 8:
        return [label]
    if " " in label:
        parts = label.split(" ")
        if len(parts) == 2:
            return parts
    if "/" in label:
        parts = label.split("/")
        if len(parts) == 2:
            return [parts[0] + "/", parts[1]]
    return [label]


def text_block(x, y, w, h, label, color):
    lines = split_label(label)
    size = 21
    if len(max(lines, key=len)) > 8:
        size = 18
    if len(max(lines, key=len)) > 12:
        size = 15
    weight = 600
    line_gap = size + 2
    total_h = line_gap * len(lines)
    start_y = y + (h - total_h) / 2 + size - 4
    pieces = []
    for i, line in enumerate(lines):
        line_y = start_y + i * line_gap
        pieces.append(
            f'<text x="{x + w/2:.1f}" y="{line_y:.1f}" '
            f'font-family="Inter, SF Pro Display, Arial, sans-serif" '
            f'font-size="{size}" font-weight="{weight}" text-anchor="middle" '
            f'fill="{color}">{html.escape(line)}</text>'
        )
    return "\n".join(pieces)


def render_layer_svg(keys, layers, meta):
    accent = meta["accent"]
    board_w = CANVAS_W - 2 * 24
    board_h = CANVAS_H - 2 * 26
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}" viewBox="0 0 {CANVAS_W} {CANVAS_H}">',
        "<defs>",
        '<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">',
        '<stop offset="0%" stop-color="#f8f9fb"/>',
        '<stop offset="100%" stop-color="#eef1f4"/>',
        "</linearGradient>",
        '<linearGradient id="case" x1="0" y1="0" x2="1" y2="1">',
        '<stop offset="0%" stop-color="#d9dde0"/>',
        '<stop offset="100%" stop-color="#bcc3c9"/>',
        "</linearGradient>",
        '<filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">',
        '<feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#89939b" flood-opacity="0.22"/>',
        "</filter>",
        "</defs>",
        f'<rect width="{CANVAS_W}" height="{CANVAS_H}" fill="url(#bg)"/>',
        f'<rect x="24" y="26" width="{board_w}" height="{board_h}" rx="34" fill="url(#case)" filter="url(#shadow)"/>',
        f'<rect x="{CANVAS_W - 148}" y="52" width="78" height="20" rx="8" fill="#2c3236" opacity="0.78"/>',
        f'<text x="62" y="46" font-family="Inter, SF Pro Display, Arial, sans-serif" font-size="15" '
        f'font-weight="700" letter-spacing="1.5" fill="#6d7982">{html.escape(meta["name"].upper())}</text>',
        f'<text x="62" y="74" font-family="Inter, SF Pro Display, Arial, sans-serif" font-size="28" '
        f'font-weight="700" fill="#202a31">{html.escape(meta["title"])}</text>',
    ]

    for key in keys:
        token = layers[key["row"] * 15 + key["col"]]
        label = format_label(token, meta["index"])
        style = key_style(token, meta["index"], accent)
        key_shadow = (
            f'<rect x="{key["x"]:.1f}" y="{key["y"] + 4:.1f}" width="{key["w"]:.1f}" height="{key["h"]:.1f}" '
            'rx="14" fill="#aeb6bd" opacity="0.18"/>'
        )
        key_rect = (
            f'<rect x="{key["x"]:.1f}" y="{key["y"]:.1f}" width="{key["w"]:.1f}" height="{key["h"]:.1f}" '
            f'rx="14" fill="{style["fill"]}" stroke="{style["stroke"]}" stroke-width="2"/>'
        )
        svg.extend([key_shadow, key_rect, text_block(key["x"], key["y"], key["w"], key["h"], label, style["text"])])

    svg.append("</svg>")
    return "\n".join(svg)


def render_png(svg_path, png_path):
    if shutil.which("sips") is None:
        return False
    subprocess.run(
        ["sips", "-s", "format", "png", str(svg_path), "--out", str(png_path)],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return True


def main():
    definition = json.loads(DEFINITION_PATH.read_text())
    layout = json.loads(LAYOUT_PATH.read_text())
    keys = parse_layout_geometry(definition)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PNG_OUT_DIR.mkdir(parents=True, exist_ok=True)

    for meta in LAYER_META:
        svg = render_layer_svg(keys, layout["layers"][meta["index"]], meta)
        svg_path = OUT_DIR / f"flow2_spacefn_layer_{meta['index']}.svg"
        svg_path.write_text(svg)
        print(svg_path.relative_to(ROOT))
        png_path = PNG_OUT_DIR / f"flow2_spacefn_layer_{meta['index']}.png"
        if render_png(svg_path, png_path):
            print(png_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
