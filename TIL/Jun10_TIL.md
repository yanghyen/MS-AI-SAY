# date
## ✅TO-DO
- ✅Category Selector 기능 구현(키워드 검색)
- Place Detail Page 디자인 && 라우팅
- 검색 페이지 수정
    - ✅usePlaceSearch 키워드로도 가능하게
    - 검색 결과 디자인
- currentLocationIcon 주변에 반투명하게 영역 표시하는 디자인

## 📌Today I Learned
### 커밋 메시지는 “왜 바꿨는지”보다 “무엇을 바꿨는지” 설명하는 게 중요

## 💡 회고 / 인사이트


## 💥 트러블슈팅
### 1. 카테고리 선택 시 마커와 리스트가 나타나지 않음
- 문제 원인
    - map을 useRef()로 관리했더니, map.current가 변경되어도 컴포넌트가 리렌더링되지 않아
    - useEffect()가 실행되지 않음 → 카테고리 검색 로직 미동작
- 해결 방법
    - map을 useState()로 관리해서 상태 변화가 생기면 useEffect()가 다시 실행되도록 수정
            
## 🍩내일 할 일
- Place Detail Page 디자인 && 라우팅
- 검색 결과 디자인
- currentLocationIcon 주변에 반투명하게 영역 표시하는 디자인