# Flow2@Lofree SpaceFn 제안 레이아웃

레이아웃 파일: `layouts/spacefn/flow2_lofree_spacefn.layout.json`

## 설계 기준

- `Layer 0/1`: Mac용
- `Layer 2/3`: Windows용
- `Layer 4/5`: 특수용
- `Space`: 탭하면 `Space`, 홀드하면 `Fn`
  - Mac: `LT(1,KC_SPC)`
  - Windows: `LT(3,KC_SPC)`
- 기존 전용 `Fn` 키 자리: `Layer 4 hold`
- `Layer 4`에서 `Left Shift`: `Layer 5 hold`
- `Caps` 위치: `Esc`
- `Esc` 위치: `` `~ ``

## 이번 변경 반영

### SpaceFn 레이어

- `Fn+1` ~ `Fn+=`: `F1` ~ `F12`
- `Fn+Q`: `Home`
- `Fn+E`: `End`
- `Fn+W/A/S/D`: `Up / Left / Down / Right`
- `Fn+H/J/K/L`: `Left / Down / Up / Right`
- `Fn+N`: Windows 레이어로 전환 (`TO(2)`)
- `Fn+M`: Mac 레이어로 전환 (`TO(0)`)
- 물리 화살표 4개: `Home / Page Down / Page Up / End`

## 레이어별 역할

### Layer 0 Mac Base

- 하단 왼쪽: `Ctrl / Command / Option`
- 하단 중앙: `SpaceFn`
- 하단 오른쪽: `Right Option / Layer 4 / Right Control`
- 물리 화살표 클러스터: `Home / Page Down / Page Up / End`

### Layer 1 Mac SpaceFn

- 숫자열: `F1` ~ `F12`
- 이동 계열:
  - `Q/E`: `Home / End`
  - `W/A/S/D`: `Up / Left / Down / Right`
  - `H/J/K/L`: `Left / Down / Up / Right`
- 시스템 전환:
  - `N`: Windows
  - `M`: Mac

### Layer 2 Windows Base

- 하단 왼쪽: `Ctrl / Alt / Win`
- 하단 중앙: `SpaceFn`
- 하단 오른쪽: `App / Layer 4 / Right Alt`
- 물리 화살표 클러스터: `Home / Page Down / Page Up / End`

### Layer 3 Windows SpaceFn

- `Layer 1`과 동일한 기능
- 우측 modifier 쪽만 Windows 배치 유지

### Layer 4 Special

기존 전용 `Fn` 키를 누르고 있는 동안 활성화.

- `1/2`: 화면 밝기 감소/증가
- `3`: 멀티 스크린
- `4`: 검색
- `5/6`: 백라이트 감소/증가
- `7/8/9/0/-/=`: 이전 곡 / 재생-일시정지 / 다음 곡 / 음소거 / 볼륨 감소 / 볼륨 증가
- `Tab`: 숫자열/F키 전환 (`CUSTOM(16)`)
- `Q/W/E/R`: BT1 / BT2 / BT3 / 2.4G 전환
- `Space`: 터치 기능 On/Off (`CUSTOM(13)`)
- `Left Arrow / Right Arrow`: 앰비언트 라이트 이전/다음 (`CUSTOM(10)`, `CUSTOM(14)`)
- `B`: NKRO 토글
- `Home / End`: `Page Up / Page Down`
- `Delete`: 잠금 추정 기능 (`CUSTOM(8)`)
- `Left Shift`: `Layer 5 hold`

### Layer 5 Deep Special

`Layer 4` 상태에서 `Left Shift`를 누르고 있는 동안 활성화.

- 좌상단: `RESET`
- `Backspace`: `QK_CLEAR_EEPROM`
- `W`: `CUSTOM(11)` 미확인

## 메모

- `Layer 4`에는 기존 무선 전환, 미디어/볼륨/밝기, 백라이트/검색/멀티스크린, 앰비언트 라이트 전환을 모아서 넣음
- `Fn+Q/E`는 `Home/End`, `Fn+WASD/HJKL`은 방향키, 물리 화살표는 `Home/PageDown/PageUp/End`로 역할을 분리함
- 탐색 계열이 중복되는 이유:
  - 문자행에서는 방향 이동을 빠르게
  - 물리 화살표에서는 문서/라인 탐색을 빠르게

## 미확인 항목

- `CUSTOM(8)`: 잠금 기능으로 추정
- `CUSTOM(11)`: 미확인
- `CUSTOM(10)`, `CUSTOM(14)`: 앰비언트 라이트 이전/다음으로 사용 유지
