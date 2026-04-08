# Flow2@Lofree 키 매핑 정리

원본 파일: `layouts/original/flow2_lofree.layout.json`

## 읽는 법

- `KC_TRNS`: 아래 레이어 값을 그대로 상속
- `KC_NO`: 미사용 슬롯 또는 물리 키가 없는 자리로 보임
- `MO(n)`: 누르고 있는 동안 레이어 `n` 활성화
- `TO(n)`: 레이어 `n`으로 전환
- `RESET`: 부트로더 리셋
- `QK_CLEAR_EEPROM`: EEPROM 초기화
- `MAGIC_TOGGLE_NKRO`: NKRO 토글

## 레이어 구성 메모

- `Layer 0`: 기본 레이어 A
- `Layer 1`: `Layer 0` 위에서 쓰는 보조 레이어
- `Layer 2`: 기본 레이어 B
- `Layer 3`: `Layer 2` 위에서 쓰는 보조 레이어
- `Layer 4`, `Layer 5`: 설정/유지보수용 보조 레이어
- 추정: `Layer 0/1`은 Windows 쪽 배치, `Layer 2/3`은 macOS 쪽 배치에 가까움

---

## Layer 0 기본 레이어 A

### Row 1

```text
`~ [KC_GRV] | 1 [KC_1] | 2 [KC_2] | 3 [KC_3] | 4 [KC_4] | 5 [KC_5] | 6 [KC_6] | 7 [KC_7] | 8 [KC_8] | 9 [KC_9] | 0 [KC_0] | - [KC_MINS] | = [KC_EQL] | Backspace [KC_BSPC] | Delete [KC_DEL]
```

### Row 2

```text
Tab [KC_TAB] | Q [KC_Q] | W [KC_W] | E [KC_E] | R [KC_R] | T [KC_T] | Y [KC_Y] | U [KC_U] | I [KC_I] | O [KC_O] | P [KC_P] | [ [KC_LBRC] | ] [KC_RBRC] | \ [KC_BSLS] | `~ [KC_GRV]
```

### Row 3

```text
Esc [KC_ESC] | A [KC_A] | S [KC_S] | D [KC_D] | F [KC_F] | G [KC_G] | H [KC_H] | J [KC_J] | K [KC_K] | L [KC_L] | ; [KC_SCLN] | ' [KC_QUOT] | 비어 있음 [KC_NO] | Enter [KC_ENT] | Home [KC_HOME]
```

### Row 4

```text
Left Shift [KC_LSFT] | 비어 있음 [KC_NO] | Z [KC_Z] | X [KC_X] | C [KC_C] | V [KC_V] | B [KC_B] | N [KC_N] | M [KC_M] | , [KC_COMM] | . [KC_DOT] | / [KC_SLSH] | Right Shift [KC_RSFT] | Up [KC_UP] | End [KC_END]
```

### Row 5

```text
Left Ctrl [KC_LCTL] | Left Alt [KC_LALT] | Left GUI/Win [KC_LGUI] | 비어 있음 [KC_NO] | 비어 있음 [KC_NO] | 비어 있음 [KC_NO] | Space [KC_SPC] | 비어 있음 [KC_NO] | 비어 있음 [KC_NO] | Caps Lock [KC_CAPS] | Layer 1 hold [MO(1)] | Right Alt [KC_RALT] | Left [KC_LEFT] | Down [KC_DOWN] | Right [KC_RGHT]
```

---

## Layer 1 보조 레이어 A

활성화: `Layer 0`에서 `MO(1)` 키를 누르고 있는 동안

`KC_TRNS`가 아닌 키만 적음.

| 기준 키 위치 | 현재 동작                       | 원본 코드           | 메모                                     |
| ------------ | ------------------------------- | ------------------- | ---------------------------------------- |
| `1`          | 화면 밝기 감소                  | `KC_BRID`           |                                          |
| `2`          | 화면 밝기 증가                  | `KC_BRIU`           |                                          |
| `3`          | 멀티 스크린                     | `CUSTOM(7)`         | 매뉴얼의 `Fn+3`                          |
| `4`          | 웹 검색                         | `KC_WWW_SEARCH`     |                                          |
| `5`          | 키보드 백라이트 감소            | `BL_DEC`            |                                          |
| `6`          | 키보드 백라이트 증가            | `BL_INC`            |                                          |
| `7`          | 이전 트랙                       | `KC_MPRV`           |                                          |
| `8`          | 재생/일시정지                   | `KC_MPLY`           |                                          |
| `9`          | 다음 트랙                       | `KC_MNXT`           |                                          |
| `0`          | 음소거                          | `KC_MUTE`           |                                          |
| `-`          | 볼륨 감소                       | `KC_VOLD`           |                                          |
| `=`          | 볼륨 증가                       | `KC_VOLU`           |                                          |
| `Backspace`  | Layer 5 hold                    | `MO(5)`             |                                          |
| `Delete`     | 잠금                            | `CUSTOM(8)`         | 매뉴얼 표 기준, Windows 쪽 기능으로 보임 |
| `Tab`        | 숫자열/F키 전환                 | `CUSTOM(16)`        | `Fn+Tab`                                 |
| `Q`          | 블루투스 디바이스 1 전환/페어링 | `0x7793`            | `Fn+Q`                                   |
| `W`          | 블루투스 디바이스 2 전환/페어링 | `0x7794`            | `Fn+W`                                   |
| `E`          | 블루투스 디바이스 3 전환/페어링 | `0x7795`            | `Fn+E`                                   |
| `R`          | 2.4G 모드 진입/페어링           | `0x7785`            | `Fn+R`                                   |
| `Home`       | Page Up                         | `KC_PGUP`           |                                          |
| `Left Shift` | Layer 4 hold                    | `MO(4)`             |                                          |
| `B`          | NKRO 토글                       | `MAGIC_TOGGLE_NKRO` |                                          |
| `N`          | Layer 2로 전환                  | `TO(2)`             |                                          |
| `M`          | 비활성/미사용                   | `KC_NO`             |                                          |
| `End`        | Page Down                       | `KC_PGDN`           |                                          |
| `Space`      | 터치 기능 On/Off                | `CUSTOM(13)`        | `Fn+Space` 3초 길게 눌러 토글            |
| `Left`       | 앰비언트 라이트 모드 이전/순환  | `CUSTOM(10)`        | `Fn+←`, Steady/Breathe/Off 순환          |
| `Right`      | 앰비언트 라이트 모드 다음/순환  | `CUSTOM(14)`        | `Fn+→`, Steady/Breathe/Off 순환          |

---

## Layer 2 기본 레이어 B

`Layer 0`와 동일한 키는 생략하고, 달라지는 키만 적음.

| 위치                    | Layer 2 동작     | 원본 코드 | Layer 0 대비                       |
| ----------------------- | ---------------- | --------- | ---------------------------------- |
| 좌상단 첫 키            | Esc              | `KC_ESC`  | Layer 0은 그레이브/틸드 (`KC_GRV`) |
| A행 첫 키               | Caps Lock        | `KC_CAPS` | Layer 0은 `Esc`                    |
| 왼쪽 하단 2번째         | Left GUI/Command | `KC_LGUI` | Layer 0은 `Left Alt`               |
| 왼쪽 하단 3번째         | Left Alt/Option  | `KC_LALT` | Layer 0은 `Left GUI/Win`           |
| 스페이스 오른쪽 첫 키   | Right Alt/Option | `KC_RALT` | Layer 0은 `Caps Lock`              |
| 스페이스 오른쪽 둘째 키 | Layer 3 hold     | `MO(3)`   | Layer 0은 `MO(1)`                  |
| 스페이스 오른쪽 셋째 키 | Right Ctrl       | `KC_RCTL` | Layer 0은 `Right Alt`              |

---

## Layer 3 보조 레이어 B

활성화: `Layer 2`에서 `MO(3)` 키를 누르고 있는 동안

대부분 `Layer 1`과 같고, 아래만 다름.

| 기준 키 위치            | Layer 3 동작     | 원본 코드 | Layer 1 대비                        |
| ----------------------- | ---------------- | --------- | ----------------------------------- |
| `N`                     | 비활성/미사용    | `KC_NO`   | Layer 1은 `TO(2)`                   |
| `M`                     | Layer 0으로 전환 | `TO(0)`   | Layer 1은 `KC_NO`                   |
| 스페이스 오른쪽 셋째 키 | Application/Menu | `KC_APP`  | Layer 1은 기본값 유지 (`Right Alt`) |

Layer 1과 동일한 나머지 변경 키:

| 기준 키 위치 | 현재 동작                       | 원본 코드           | 메모                                     |
| ------------ | ------------------------------- | ------------------- | ---------------------------------------- |
| `1`          | 화면 밝기 감소                  | `KC_BRID`           |                                          |
| `2`          | 화면 밝기 증가                  | `KC_BRIU`           |                                          |
| `3`          | 멀티 스크린                     | `CUSTOM(7)`         | 매뉴얼의 `Fn+3`                          |
| `4`          | 웹 검색                         | `KC_WWW_SEARCH`     |                                          |
| `5`          | 키보드 백라이트 감소            | `BL_DEC`            |                                          |
| `6`          | 키보드 백라이트 증가            | `BL_INC`            |                                          |
| `7`          | 이전 트랙                       | `KC_MPRV`           |                                          |
| `8`          | 재생/일시정지                   | `KC_MPLY`           |                                          |
| `9`          | 다음 트랙                       | `KC_MNXT`           |                                          |
| `0`          | 음소거                          | `KC_MUTE`           |                                          |
| `-`          | 볼륨 감소                       | `KC_VOLD`           |                                          |
| `=`          | 볼륨 증가                       | `KC_VOLU`           |                                          |
| `Backspace`  | Layer 5 hold                    | `MO(5)`             |                                          |
| `Delete`     | 잠금                            | `CUSTOM(8)`         | 매뉴얼 표 기준, Windows 쪽 기능으로 보임 |
| `Tab`        | 숫자열/F키 전환                 | `CUSTOM(16)`        | `Fn+Tab`                                 |
| `Q`          | 블루투스 디바이스 1 전환/페어링 | `0x7793`            | `Fn+Q`                                   |
| `W`          | 블루투스 디바이스 2 전환/페어링 | `0x7794`            | `Fn+W`                                   |
| `E`          | 블루투스 디바이스 3 전환/페어링 | `0x7795`            | `Fn+E`                                   |
| `R`          | 2.4G 모드 진입/페어링           | `0x7785`            | `Fn+R`                                   |
| `Home`       | Page Up                         | `KC_PGUP`           |                                          |
| `Left Shift` | Layer 4 hold                    | `MO(4)`             |                                          |
| `B`          | NKRO 토글                       | `MAGIC_TOGGLE_NKRO` |                                          |
| `End`        | Page Down                       | `KC_PGDN`           |                                          |
| `Space`      | 터치 기능 On/Off                | `CUSTOM(13)`        | `Fn+Space` 3초 길게 눌러 토글            |
| `Left`       | 앰비언트 라이트 모드 이전/순환  | `CUSTOM(10)`        | `Fn+←`, Steady/Breathe/Off 순환          |
| `Right`      | 앰비언트 라이트 모드 다음/순환  | `CUSTOM(14)`        | `Fn+→`, Steady/Breathe/Off 순환          |

---

## Layer 4 설정 레이어

활성화: `Layer 1/3`에서 `Left Shift` 자리에 있는 `MO(4)`를 누르고 있는 동안

`KC_TRNS`가 아닌 키만 적음.

| 기준 키 위치 | 현재 동작     | 원본 코드         | 메모             |
| ------------ | ------------- | ----------------- | ---------------- |
| 좌상단 첫 키 | Reset         | `RESET`           | 부트로더 리셋    |
| `Backspace`  | EEPROM 초기화 | `QK_CLEAR_EEPROM` | 설정 초기화 성격 |
| `W`          | 미확인 커스텀 | `CUSTOM(11)`      |                  |

---

## Layer 5 설정 레이어

활성화: `Layer 1/3`에서 `Backspace` 자리에 있는 `MO(5)`를 누르고 있는 동안

`KC_TRNS`가 아닌 키만 적음.

| 기준 키 위치 | 현재 동작     | 원본 코드         | 메모                  |
| ------------ | ------------- | ----------------- | --------------------- |
| `Left Shift` | EEPROM 초기화 | `QK_CLEAR_EEPROM` | Layer 4와 역할이 겹침 |

---

## 미확인 키 정리용 메모

아래 표는 매뉴얼과 현재 레이아웃만으로 의미를 끝까지 확정하지 못한 키들이다. 여기에 직접 채워 넣으면 된다.

| 코드         | 위치                 | 현재 추정/설명                               | 사용자 메모 |
| ------------ | -------------------- | -------------------------------------------- | ----------- |
| `CUSTOM(8)`  | Layer 1/3의 `Delete` | 잠금 기능으로 추정, Windows 기준일 가능성 큼 |             |
| `CUSTOM(10)` | Layer 1/3의 `Left`   | 앰비언트 라이트 모드 순환의 한 방향          |             |
| `CUSTOM(11)` | Layer 4의 `W`        | 미확인 커스텀                                |             |
| `CUSTOM(14)` | Layer 1/3의 `Right`  | 앰비언트 라이트 모드 순환의 한 방향          |             |

## 추가 메모

- `KC_NO`가 있는 자리는 실제로는 키가 없는 더미 슬롯일 가능성이 큼
- `Layer 1`과 `Layer 3`는 거의 같은데, 레이어 전환 키 위치만 다름
- `Layer 4/5`는 실사용 레이어라기보다 설정/복구용에 가까워 보임
- 매뉴얼 기준으로 확인된 기능:
  - `Fn+Q/W/E`: 블루투스 디바이스 1/2/3 전환 또는 페어링
  - `Fn+R`: 2.4G 모드 진입/페어링
  - `Fn+Tab`: 숫자열/F키 전환
  - `Fn+Space` 3초: 측면 터치 기능 On/Off
  - `Fn+←/→`: 앰비언트 라이트 모드 순환
  - `Fn+Left Shift+Backspace`: 공장 초기화
