# Typescript + Vite + React(yarn)
### 과정
1. 프로젝트 생성
    - ```yarn create vite may29_typescript-test --template react-ts```
    - ```cd may29_typescript-test```
    - ```yarn```
    - ```yarn dev``` <- 시작 명령어
2. App.tsx 수정
```js
function App () {...}   // 을
const App:React.FC = () => {     // 로 Function Component 리턴하겠다
```

