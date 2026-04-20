# Firmware Artifacts

## Patched

- [patched/oe928_v14_spacefn.hex](patched/oe928_v14_spacefn.hex)

Patched vendor `v14` firmware with the SpaceFn default layout embedded.

## Extracted

- [extracted/oe928_v14_factory.layout.json](extracted/oe928_v14_factory.layout.json)

VIA save-format layout extracted from the vendor `v14` firmware image.

## Notes

- The patched firmware was generated from [../references/oe928_v14_vendor.hex](../references/oe928_v14_vendor.hex) using [../tools/oe928_firmware_tool.py](../tools/oe928_firmware_tool.py).
- The extracted layout reflects the embedded factory default from vendor firmware `v14`, which is not identical to the repo backup in `layouts/original/`.
