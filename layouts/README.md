# Layouts

This directory contains VIA save-format layouts used by this repo.

## Files

- [original/flow2_lofree.layout.json](original/flow2_lofree.layout.json): repo backup of the original layout that was used as a starting point
- [spacefn/flow2_lofree_spacefn.layout.json](spacefn/flow2_lofree_spacefn.layout.json): main SpaceFn layout for daily use

## Notes

- The `original` layout is useful as a human-readable backup, but it is not a byte-for-byte extraction of the embedded default keymap from vendor firmware `v14`.
- The extracted embedded default from the vendor firmware lives in [../firmware/extracted/oe928_v14_factory.layout.json](../firmware/extracted/oe928_v14_factory.layout.json).
- VIA `Save + Load` can turn some Flow 2 wireless switching keys into `KC_NO`. For the most reliable result, use the patched firmware in [../firmware/patched/oe928_v14_spacefn.hex](../firmware/patched/oe928_v14_spacefn.hex).
