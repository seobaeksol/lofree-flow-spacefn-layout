# Flash The Patched Firmware

This is the recommended workflow for the Flow 2 68-key (`OE928`).

It keeps the vendor firmware base intact while replacing only the embedded default keymap.

## Files You Need

- [../../firmware/patched/oe928_v14_spacefn.hex](../../firmware/patched/oe928_v14_spacefn.hex)
- [../../references/oe928_v14_vendor.hex](../../references/oe928_v14_vendor.hex) for rollback
- QMK Toolbox

## Why This Path Is Recommended

The Flow 2 stores some wireless-switching keys in a way that does not round-trip cleanly through VIA `Save + Load`.

Flashing the patched vendor firmware avoids that problem because the correct default keycodes are embedded directly in the firmware image.

## Before You Flash

- back up anything you care about
- keep the original vendor firmware file
- connect the keyboard over USB
- make sure you know the vendor DFU entry procedure

## Flash Steps

1. Open QMK Toolbox.
2. Load [../../firmware/patched/oe928_v14_spacefn.hex](../../firmware/patched/oe928_v14_spacefn.hex).
3. Put the keyboard into DFU mode using the vendor upgrade procedure.
4. Click `Flash`.
5. Wait until the flash completes and the keyboard reboots.

## After Flashing

If the keyboard still behaves like the old layout, clear EEPROM.

For the layouts in this repo, the maintenance shortcut is:

- hold the hardware `Fn` key
- hold `Left Shift`
- press `Backspace`

That triggers `QK_CLEAR_EEPROM`.

## Verify

Test at least these keys:

- tap `Space`: normal space
- hold `Space` + `W/A/S/D`: arrows
- hold `Space` + `Q/E`: `Home/End`
- hardware `Fn` + `Q/W/E/R`: `BT1 / BT2 / BT3 / 2.4G`

## Rollback

If you want to return to the vendor firmware, flash:

- [../../references/oe928_v14_vendor.hex](../../references/oe928_v14_vendor.hex)

Then clear EEPROM again.

## Rebuild The Patched HEX

If you edit the SpaceFn VIA layout file, regenerate the firmware with:

```bash
make patch
```
