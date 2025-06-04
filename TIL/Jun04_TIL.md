# date
## ✅TO-DO
- ✅전체 플로우 손 그림 디자인(User Page 안 함)
- ✅Main Page 디자인
- ✅전체 페이지 라우팅
    - Detail Page는 제외
- Road View Page 구현
    - 외않되
- Search Page 디자인
- 메인화면에서 Bottom Panel에 어떤 정보 넣을지? 
    - 메인화면에서 제외해도 ㄱㅊ을지도
    - 인기 급상승 데이터를 여기에 넣어도 ㄱㅊ다

## 📌Today I Learned
### React + Vite 이미지 불러오기
- React + Vite에서 이미지를 불러올 땐 ```impot```를 해야 한다. 
```js
import currentLocationIcon from '../assets/current_location.png';

<img src={currentLocationIcon} alt="내 위치" style={{ width: 30, height: 30 }} />
```

## 💡 회고 / 인사이트
- 아니 작업 하나 끝날 때마다 커밋하기로 한 거 또 깜빡했다. 
- App.tsx에 라우터 했던 거 router/index.ts으로 옮겨서 정리했다. 이게 유지보수가 편하다고 한다.
            
## 🍩내일 할 일
- Road View Page 구현
- Search Page 디자인
- Detail Page 디자인 && 라우팅