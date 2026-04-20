PYTHON ?= python3

TOOL := tools/oe928_firmware_tool.py
VENDOR_HEX := references/oe928_v14_vendor.hex
SPACEFN_LAYOUT := layouts/spacefn/flow2_lofree_spacefn.layout.json
PATCHED_HEX := firmware/patched/oe928_v14_spacefn.hex
EXTRACTED_LAYOUT := firmware/extracted/oe928_v14_factory.layout.json

.PHONY: dump extract patch

dump:
	$(PYTHON) $(TOOL) dump --decode "$(VENDOR_HEX)"

extract:
	$(PYTHON) $(TOOL) extract "$(VENDOR_HEX)" "$(EXTRACTED_LAYOUT)"

patch:
	$(PYTHON) $(TOOL) patch "$(VENDOR_HEX)" "$(SPACEFN_LAYOUT)" "$(PATCHED_HEX)"
