# References

This directory stores vendor files and supporting material used to analyze or patch the Flow 2 firmware.

## Files

- [oe928_v14_vendor.hex](oe928_v14_vendor.hex): original vendor firmware used as the patching base and rollback target
- [oe928_via_definition_20251114.json](oe928_via_definition_20251114.json): VIA definition file used with this board
- [lofree_flow2_manual.pdf](lofree_flow2_manual.pdf): product manual
- [flow2_upgrade_instructions.mp4](flow2_upgrade_instructions.mp4): vendor flashing guide video

## Notes

- Treat [oe928_v14_vendor.hex](oe928_v14_vendor.hex) as the source-of-truth firmware artifact in this repo.
- If you need to undo the SpaceFn firmware, flashing the original vendor HEX is safer than relying on a VIA layout restore.
- Generated outputs do not belong here. Patched firmware and extracted layouts live under [../firmware/](../firmware/).
