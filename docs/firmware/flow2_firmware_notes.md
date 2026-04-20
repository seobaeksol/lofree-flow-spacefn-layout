# Flow 2 Firmware Notes

Reverse-engineering notes for the 68-key Flow 2 (`OE928`) based on:

- vendor firmware: [../../references/oe928_v14_vendor.hex](../../references/oe928_v14_vendor.hex)
- vendor VIA definition: [../../references/oe928_via_definition_20251114.json](../../references/oe928_via_definition_20251114.json)
- vendor upgrade guide: [../../references/flow2_upgrade_instructions.mp4](../../references/flow2_upgrade_instructions.mp4)
- external reference: [piperamirez/lofree-flow2-os9-driver](https://github.com/piperamirez/lofree-flow2-os9-driver)

## Confirmed Facts

- The Flow 2 68-key firmware image is an ARM Intel HEX image mapped at `0x08000000`.
- The upgrade flow uses **WB32 DFU** through QMK Toolbox. The guide video shows `wb32-dfu-updater_cli`.
- The upgrade log in the guide reports `256 KBytes` flash and `36 KBytes` SRAM, which matches Westberry's `WB32FQ95xx` family closely.
- The embedded USB descriptor contains `VID/PID = 0x388D / 0x0001`.
- The firmware includes a 6-layer default keymap block at `0x0800E574`.

## What The OS 9 Driver Confirms

The external Mac OS 9 driver is for the **Flow 2 2.4G dongle**, not the keyboard firmware itself, but it still confirms useful USB facts:

- The dongle also uses `VID/PID = 0x388D / 0x0001`.
- Interface 0 is a standard HID boot keyboard (`class 3 / subclass 1 / protocol 1`).
- The device is composite and exposes at least interfaces 1 and 2 in addition to the boot keyboard interface.
- Caps Lock LED output uses an interrupt OUT endpoint with payload `[0x01, ledByte]`, where `0x01` is the HID report ID.

Implication:

- `0x388D:0x0001` is not enough to mean "wired mode only".
- Patching the vendor firmware's embedded keymap is much safer than replacing the whole USB stack, because it keeps the vendor's existing WB32 bootloader and USB/wireless behaviour intact.

## Keycode Notes

- The VIA save files in this repo store Flow 2 wireless switching as raw QMK connection keycodes:
  - `0x7793` = `QK_BLUETOOTH_PROFILE1`
  - `0x7794` = `QK_BLUETOOTH_PROFILE2`
  - `0x7795` = `QK_BLUETOOTH_PROFILE3`
  - `0x7785` = `QK_OUTPUT_2P4GHZ`
- In the factory `v14` firmware image, those four positions are stored as internal `QK_KB_*` slots:
  - `0x7E01`, `0x7E02`, `0x7E03`, `0x7E04`
- That explains why raw values from VIA do not round-trip cleanly through all tooling, while the vendor firmware still restores working BT/2.4G defaults.

## Extracted Default vs Repo Backup

Using the embedded keymap extractor on the vendor `v14` HEX shows that the firmware default is not identical to [../../layouts/original/flow2_lofree.layout.json](../../layouts/original/flow2_lofree.layout.json).

Current known differences are small but real:

- layer 0 top-left is `KC_ESC` in the vendor firmware, not `KC_GRV`
- layer 0 also shifts `KC_CAPS` / `KC_RGUI` positions accordingly
- layer 4 index 15 contains an unknown internal keycode `0x7E00`

Implication:

- `layouts/original/flow2_lofree.layout.json` should be treated as a useful backup, not necessarily a byte-for-byte export of the factory `v14` image.

## Practical Path

Today the realistic paths are:

1. Patch the vendor `v14` firmware's embedded default keymap and flash it with QMK Toolbox.
2. Reset EEPROM after flashing so the patched defaults are actually loaded.
3. Attempt a full QMK port only after confirming:
   - MCU exact model
   - matrix pins and diode direction
   - wired vs dongle VID/PID behaviour
   - wireless feature implementation

## Tooling In This Repo

[../../tools/oe928_firmware_tool.py](../../tools/oe928_firmware_tool.py) currently supports:

- `dump`: print the embedded 6-layer default keymap from the vendor HEX
- `dump --decode`: print decoded QMK/VIA-style tokens
- `extract`: export the embedded default keymap as a VIA save JSON
- `patch`: write a VIA save JSON back into the vendor HEX

Examples:

```bash
python3 tools/oe928_firmware_tool.py dump --decode 'references/oe928_v14_vendor.hex'
python3 tools/oe928_firmware_tool.py extract 'references/oe928_v14_vendor.hex' 'firmware/extracted/oe928_v14_factory.layout.json'
python3 tools/oe928_firmware_tool.py patch 'references/oe928_v14_vendor.hex' 'layouts/spacefn/flow2_lofree_spacefn.layout.json' 'firmware/patched/oe928_v14_spacefn.hex'
```
