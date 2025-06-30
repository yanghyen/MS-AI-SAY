# 250530
## ✅TO-DO
- ✅타입스크립트 강의 듣기  
- 프론트엔드 초기 세팅
    - ✅typescript + vite + yarn 프로젝트 생성
    - ✅디렉토리 구조 
    - ✅gitHub 레포 생성 및 git init
- 메인화면 페이지

## 📌Today I Learned
### 프론트엔드 디렉토리 구조 및 개발 순서
- 디렉토리 구조
```txt
src/
│
├── assets/            # 이미지, 폰트 등 정적 파일
├── components/        # 재사용 가능한 UI 컴포넌트들
├── pages/             # 라우트 단위 페이지
├── layouts/           # 페이지 레이아웃 (공통 구조)
├── hooks/             # 커스텀 훅
├── utils/             # 공통 유틸 함수
├── api/               # API 호출 정리 (ex. axios instance)
├── stores/            # 상태관리 (zustand, recoil 등)
├── model/             # 타입 정의 (ex. interface, type)
├── constants/         # 상수 모음 (ex. routes, colors)
├── router/            # React Router 설정
├── styles/            # 글로벌 스타일, 테마
└── main.tsx           # 진입점 (App 렌더링)

```
- 개발 순서
    -  페이지 개발 + 기능 연결
        - 페이지별 디렉토리 생성 후 실제 기능 구현
        - 컴포넌트 → 레이아웃 → API 연동 → 전역 상태 순서로 연결

### Vite에 동적으로 Kakao SDK 불러오기
- JS는 public/index.html에 ```<script src="kakao api url" ~~~>```을 추가해서 api key도 입력했었다.
- Vite는 동적으로 불러오는 걸 권장한다.
```js
// MapView.tsx
export default function MapView() {
  useEffect(() => {
    const loadKakaoMap = () => {
      const script = document.createElement("script")
      script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${import.meta.env.VITE_KAKAO_MAP_KEY}&autoload=false&libraries=services`
      script.onload = () => {
```

### unused var, type 'any' error 뜰 때
- TypeScript 자체의 문제가 아니라, ESLint 규칙 설정 때문
- eslint.config.js에 error -> warn로 바꿔주면 됨
- 기본값이 error인 거라 warn으로 수정한 코드 추가하면 됨
```js
rules: {
    ...reactHooks.configs.recommended.rules,
    'react-refresh/only-export-components': [
    'warn',
    { allowConstantExport: true },
    ],
    '@typescript-eslint/no-explicit-any': 'warn',
    '@typescript-eslint/no-unused-vars': 'warn',
```

## 💡 회고 / 인사이트
타입스크립트가 생각보다 까다롭다. 그리고 새로운 언어로 개발할 때 디렉토리 구조 파악하는 게 제일 어렵지만 중요한 것 같다. 타입스크립트 디렉토리 구조를 최대한 유지보수 쉽게 처리하려고 하다보니 디렉토리로 나눠서 어렵다. 하지만 이해하면서 하다보면 나중에 더 편하겠지~! 역시 새로운 걸 배우고 디벨롭해가는 건 재밌다. react로 프론트 개발한지 얼마 되지 않았지만 typescriptㄹ 해나가는 게 재밌다. 나중엔 더 익숙해져있겠징. 화이팅~

## 🍩내일 할 일
- 메인 페이지에 지도 띄우기(카카오api SDK 로드 안되는 거 해결해야 됨)