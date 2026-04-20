# Lofree Flow / Flow2 SpaceFn

**Lofree Flow 2 68키 (`OE928`)**를 위한 SpaceFn 레이아웃, 패치된 제조사 펌웨어, 분석 도구를 정리한 저장소입니다.

English README: [README.md](README.md)

## 먼저 여기부터

가장 간단한 방법은 [firmware/patched/oe928_v14_spacefn.hex](firmware/patched/oe928_v14_spacefn.hex)를 그대로 플래시하는 것입니다.

이 방법을 추천하는 이유는 Flow 2의 무선 전환 키를 VIA `Save + Load`에 의존하지 않고 안정적으로 유지할 수 있기 때문입니다.

## 이 펌웨어로 얻는 키맵

이 펌웨어는 SpaceFn 기반 키맵에 제조사 무선 전환 키를 그대로 유지한 구성입니다.

- `Space` 짧게 누름: 일반 스페이스
- `Space` 길게 누름: 임시 Fn 레이어
- `Fn + W A S D`: 방향키
- `Fn + H J K L`: 방향키
- `Fn + Q / E`: `Home / End`
- `Fn + 1..=`: `F1..F12`
- 물리 방향키 4개: `Home / Page Down / Page Up / End`
- 특수 레이어에 BT1 / BT2 / BT3 / 2.4G 전환 유지

전체 레이어 설명은 [docs/keymaps/flow2_lofree_spacefn_keymap.md](docs/keymaps/flow2_lofree_spacefn_keymap.md)를 보면 됩니다.

## 필요한 것

- **Lofree Flow 2 68키 (`OE928`)**
- USB 케이블
- 플래시용 [QMK Toolbox](https://github.com/qmk/qmk_toolbox/releases)
- 선택 사항: 플래시 후 레이아웃 확인이나 수정용 [VIA](https://usevia.app/)
- 사용할 펌웨어 파일: [firmware/patched/oe928_v14_spacefn.hex](firmware/patched/oe928_v14_spacefn.hex)

참고 링크:

- [QMK 기본 플래시 가이드](https://docs.qmk.fm/newbs_flashing)
- [QMK 부트로더 / 플래싱 문서](https://docs.qmk.fm/flashing)
- 이 저장소에 포함된 제조사 가이드 영상: [references/flow2_upgrade_instructions.mp4](references/flow2_upgrade_instructions.mp4)

## 펌웨어 플래시 방법

1. [QMK Toolbox](https://github.com/qmk/qmk_toolbox/releases)를 설치합니다.
2. QMK Toolbox를 열고 [firmware/patched/oe928_v14_spacefn.hex](firmware/patched/oe928_v14_spacefn.hex)를 불러옵니다.
3. 키보드를 DFU 모드로 진입시킵니다. 방법을 모르겠으면 [references/flow2_upgrade_instructions.mp4](references/flow2_upgrade_instructions.mp4)를 참고합니다.
4. QMK Toolbox에서 `Flash`를 누르고 완료될 때까지 기다립니다.
5. 키보드가 다시 올라오면 EEPROM을 초기화해서 새 기본 레이아웃이 적용되게 합니다.
6. `SpaceFn`, 방향키 레이어, BT1 / BT2 / BT3 / 2.4G 전환이 정상 동작하는지 확인합니다.

전체 절차는 [docs/guides/flash_patched_firmware.md](docs/guides/flash_patched_firmware.md)에 더 자세히 정리되어 있습니다.

## 제조사 펌웨어로 되돌리기

SpaceFn 펌웨어를 되돌리고 싶으면 같은 방식으로 [references/oe928_v14_vendor.hex](references/oe928_v14_vendor.hex)를 플래시하면 됩니다.

## 제조사 펌웨어 유지 + VIA만 사용하고 싶다면

VIA만 써도 됩니다.

- [layouts/spacefn/flow2_lofree_spacefn.layout.json](layouts/spacefn/flow2_lofree_spacefn.layout.json) 불러오기
- [docs/guides/via_layouts.md](docs/guides/via_layouts.md)의 주의사항 확인

다만 이 방식은 Flow 2 무선 전환 키가 VIA `Save + Load` 왕복 과정에서 `KC_NO`로 바뀔 수 있어서 패치 펌웨어보다 덜 안정적입니다.

## 이 저장소가 제공하는 것

- Flow 2 68키용 **SpaceFn** 레이아웃
- 이 저장소에서 사용한 원본 VIA 레이아웃 백업
- BT/2.4G 전환 키가 정상 유지되도록 패치한 제조사 펌웨어
- 제조사 펌웨어 안의 기본 키맵을 추출/패치하는 도구
- 왜 VIA `Save + Load`만으로는 일부 키가 `KC_NO`가 되는지에 대한 정리

## 왜 SpaceFn인가

핵심 아이디어는 하나입니다.

- `Space` 짧게 누름: 일반 스페이스
- `Space` 길게 누름: 임시 Fn 레이어

SpaceFn 레이어에서 제공하는 주요 기능:

- `Fn + W A S D`: 방향키
- `Fn + H J K L`: 방향키
- `Fn + Q / E`: `Home / End`
- `Fn + 1..=`: `F1..F12`
- 물리 방향키 4개: `Home / Page Down / Page Up / End`
- 무선 전환, 미디어, 볼륨, 밝기, 백라이트, 검색, 앰비언트 라이트용 특수 레이어

## 저장소 구성

- [layouts/original/flow2_lofree.layout.json](layouts/original/flow2_lofree.layout.json): 원본 VIA 레이아웃 백업
- [layouts/spacefn/flow2_lofree_spacefn.layout.json](layouts/spacefn/flow2_lofree_spacefn.layout.json): 메인 SpaceFn 레이아웃
- [layouts/README.md](layouts/README.md): 레이아웃 출처와 주의사항 정리
- [firmware/patched/oe928_v14_spacefn.hex](firmware/patched/oe928_v14_spacefn.hex): 바로 플래시 가능한 패치 펌웨어
- [firmware/extracted/oe928_v14_factory.layout.json](firmware/extracted/oe928_v14_factory.layout.json): 제조사 `v14` 펌웨어에서 추출한 기본 레이아웃
- [tools/oe928_firmware_tool.py](tools/oe928_firmware_tool.py): 펌웨어 추출/패치 도구
- [docs/README.md](docs/README.md): 문서 인덱스
- [references/README.md](references/README.md): 제조사 파일과 분석 참고 자료

## 중요한 메모

- Flow 2 68키는 일부 무선 전환 키를 제조사 전용 방식으로 처리합니다.
- 그래서 VIA 레이아웃 JSON만으로는 해당 키를 항상 안정적으로 보존할 수 없습니다.
- [layouts/original/flow2_lofree.layout.json](layouts/original/flow2_lofree.layout.json)은 유용한 백업이지만, 제조사 `v14` 펌웨어의 내장 기본 레이아웃과 완전히 동일한 덤프는 아닙니다.

## 도구 사용

포함된 도구로 할 수 있는 작업:

- 제조사 펌웨어의 기본 키맵 덤프
- 덤프를 VIA/QMK 스타일 토큰으로 해석
- VIA 레이아웃 JSON으로 추출
- VIA 레이아웃 JSON을 다시 제조사 펌웨어에 패치

자주 쓰는 명령:

```bash
make dump
make extract
make patch
```

## 문서

- [docs/README.md](docs/README.md)
- [docs/guides/flash_patched_firmware.md](docs/guides/flash_patched_firmware.md)
- [docs/guides/via_layouts.md](docs/guides/via_layouts.md)
- [docs/firmware/flow2_firmware_notes.md](docs/firmware/flow2_firmware_notes.md)
- [docs/keymaps/flow2_lofree_spacefn_keymap.md](docs/keymaps/flow2_lofree_spacefn_keymap.md)
