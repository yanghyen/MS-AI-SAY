# Typescript
## 자료형
- number
- string
- boolean
- null
- undefined
- any: 어떤 타입일지 모를 때(잘 안 씀)

### 변수 선언
```typescript
let a:number = 10
a = "asdf"  // 에러남
a = 4

let b:any = 4
b = "asdf"  // any type이라 에러는 안 남

let c:number | string = "asdf"
c = 3   // 둘 중 하나만 오면 가능
```

### 배열
```typescript
let e:string[] = ['apple', 'banana']    // array인데 string
```

### 객체
- 는 따로 만들어서 씀!
1. type 선언
```js
export type Restaurant = {
    name:string;
    category:string;
    address:Address;
    menu:Menu[]
}

export type Address = {     // type의 type도 생성 가능
    city:string;
    detail:string;
    zipCode:number
}
```
2. interface 생성
### 함수
```typescript
function addNumber (a:number, b:number):number{ // number, number 받고, number return함
    return a+b
}

// 제네릭 문법
// useState를 이 타입으로 지정하겠다
// setMyRestaurant(); 호출 시 타입 맞춰야 함
import type {Restaurant} from './model/restaurant'; // import type으로 type 가져오기
const [myRestaurant, setMyRestaurant] = useState<Restaurant>(data)
```
## 실행
### tsconfig.json
```json
{
    // TypeScript 컴파일러의 옵션들을 지정하는 속성
    "compilerOptions": { 
        "outDir": "dist",
        "target": "es6", 
        "module": "commonjs",
        "lib" : ["es6"],
    "sourceMap": true
    
    },

}
```
### 빌드
- Mac : VSCode에서 ```cmd + shift + B``` 후 tsconfig.json 선택하면 빌드됨
- Window : VSCode에서 하면 안됨!
    - cmd에서 명령어로 실행
    - ```tsc -p tsconfig.json --watch```
    