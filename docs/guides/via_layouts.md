# Use VIA Layouts Only

This path works, but it has an important caveat on the Flow 2 68-key.

## The Caveat

`usevia.app` does not reliably preserve the Flow 2 wireless-switching keys through `Save + Load` when they are stored as raw connection keycodes.

The affected keys are:

- `0x7793`: Bluetooth profile 1
- `0x7794`: Bluetooth profile 2
- `0x7795`: Bluetooth profile 3
- `0x7785`: 2.4G

When the round-trip fails, those keys often come back as `KC_NO`.

## When VIA Is Still Fine

VIA is still useful if:

- you want to experiment without reflashing firmware
- you do not touch the wireless-switching keys
- you are willing to re-enter those four values manually after loading

## Suggested VIA Workflow

1. Start from [../../layouts/spacefn/flow2_lofree_spacefn.layout.json](../../layouts/spacefn/flow2_lofree_spacefn.layout.json).
2. Load it into VIA.
3. Check the hardware `Fn` layer `Q/W/E/R` keys immediately.
4. If they show up as `KC_NO`, set them manually to:
   - `0x7793`
   - `0x7794`
   - `0x7795`
   - `0x7785`

## When To Prefer Patched Firmware

Use the patched firmware instead if:

- you want a stable setup that survives resets
- you want the repo's SpaceFn layout exactly as tested
- you do not want to fix BT/2.4G keys manually in VIA

Recommended guide:

- [flash_patched_firmware.md](flash_patched_firmware.md)
