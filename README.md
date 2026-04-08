# Lofree Flow / Flow2 SpaceFn Layout

Custom VIA layouts for the Lofree Flow / Flow2 keyboard, built around a SpaceFn workflow for development-heavy use.

Korean README: [README.ko.md](README.ko.md)

## Why I made this

As a developer, I kept tuning my keyboard layout around the things I use constantly while writing code:

- arrow movement
- `Home` / `End`
- `Page Up` / `Page Down`
- function keys
- fast macOS / Windows switching

So I ended up building a custom VIA layout for the Lofree Flow / Flow2 with one main idea:

- tap `Space`: normal space
- hold `Space`: temporary Fn layer

The goal was simple: reduce hand movement without turning the layout into something awkward to daily-drive.

## Main ideas

- `Fn + W A S D`: arrow keys
- `Fn + H J K L`: arrow keys
- `Fn + Q / E`: `Home / End`
- physical arrow cluster: `Home / Page Down / Page Up / End`
- `Fn + 1..=`: `F1..F12`
- `Fn + M / N`: macOS / Windows layer switching
- dedicated hardware `Fn` key: special layer access
- wireless switching, media, volume, brightness, backlight, search, multi-screen, and ambient light controls are grouped into a separate special layer

## Repository structure

- `layouts/original/flow2_lofree.layout.json`
  - original layout backup
- `layouts/spacefn/flow2_lofree_spacefn.layout.json`
  - current custom layout
- `docs/keymaps/`
  - detailed layer notes and mapping docs
- `references/lofree_flow2_manual.pdf`
  - manual used to identify vendor-specific keycodes

## Notes

- This repo is intentionally lightweight. The detailed explanation lives in `docs/keymaps/`.
- Additional suggestions are always welcome.
- If you know the meaning of any still-unidentified custom keycodes, I would appreciate it if you let me know.

## Status

- The layout is already usable and feels better than I expected in real work.
- It is still evolving, especially around vendor-specific custom keys and small ergonomic refinements.
