# Lofree Flow / Flow2 SpaceFn 레이아웃

개발 작업 흐름에 맞춰 다듬은 Lofree Flow / Flow2용 VIA 커스텀 레이아웃 저장소입니다.

English README: [README.md](README.md)

## 왜 만들었나

개발자로 일하다 보니 결국 자주 손이 가는 키들이 거의 정해져 있었습니다.

- 방향키
- `Home` / `End`
- `Page Up` / `Page Down`
- 펑션키
- macOS / Windows 전환

그래서 Lofree Flow / Flow2에서 손 이동을 줄이면서도 일상적으로 쓰기 불편하지 않은 방향으로 레이아웃을 직접 구성해봤습니다.

핵심 컨셉은 `SpaceFn`입니다.

- `Space` 짧게 누름: 일반 스페이스
- `Space` 길게 누름: 임시 Fn 레이어

## 이 레이아웃의 특징

- `Fn + W A S D`: 방향키
- `Fn + H J K L`: 방향키
- `Fn + Q / E`: `Home / End`
- 물리 방향키 4개: `Home / Page Down / Page Up / End`
- `Fn + 1..=`: `F1..F12`
- `Fn + M / N`: macOS / Windows 레이어 전환
- 전용 하드웨어 `Fn` 키: 특수 레이어 진입
- 무선 전환, 미디어, 볼륨, 밝기, 백라이트, 검색, 멀티스크린, 앰비언트 라이트 기능은 별도 특수 레이어로 분리

## 저장소 구성

- `layouts/original/flow2_lofree.layout.json`
  - 원본 레이아웃 백업
- `layouts/spacefn/flow2_lofree_spacefn.layout.json`
  - 현재 메인 커스텀 레이아웃
- `docs/keymaps/`
  - 레이어별 상세 설명 문서
- `references/lofree_flow2_manual.pdf`
  - 제조사 전용 키코드 확인에 참고한 매뉴얼

## 메모

- 자세한 설명은 `docs/keymaps/`에 따로 정리해두었습니다.
- 추가적인 제안 사항은 언제나 환영입니다.
- 아직 정확히 의미를 모르는 커스텀 키들이 있는데, 아시는 분이 알려주시면 감사하겠습니다.

## 현재 상태

- 실사용 가능한 상태이고, 예상보다 꽤 만족스럽게 쓰고 있습니다.
- 다만 제조사 전용 커스텀 키와 자잘한 사용성 부분은 계속 다듬어갈 생각입니다.
