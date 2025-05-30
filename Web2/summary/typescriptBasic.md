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
```js
// info:Restaurant라서 info가 Restaurant로 들어옴
interface OwnProps {
    info:Restaurant,
    changeAddress(address:Address):void // return값이 없어서 void
}
const Store:React.FC<OwnProps> = ({info, changeAddress}) => {
```

### extends
- 타입 선언한 거 가져오기
```js
interface OwnProps extends Menu {
    showBestMenuName(name:string):string    // Menu에 지정 안된 타입 추가도 가능
}
```
- Omit : 타입에서 뭔가를 빼고 가져오기 
```js
// Omit : 이거 빼주세용
export type AddressWithoutZip = Omit<Address, 'zipCode'>

// 함수에서 바로 쓰기도 가능
interface OwnProps extends Omit<Menu, 'price'> {}
```
- Pick : 타입에서 특정 값만 가져오기
```js
export type RestaurantOnlyCategory = Pick<Restaurant, 'category'>
```

### API call 타입 만들기
```js
export type ApiResponse<T> = {
    data:T[],       // data가 api 호출에 따라 타입이 달라지니까
    totlaPage:number,
    page:number
}

export type RestaurantResponse = ApiResponse<Restaurant>
export type MenuResponse = ApiResponse<Menu>
```

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
    