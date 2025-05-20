# React Event
## source/may20_1/src/event/* 참고
## 마우스 이벤트
### 마우스 좌표
- html 기준 마우스 좌표 : e.clientX, e.clientY
- 객체 기준 마우스 좌표 : e.nativeEvent.offsetX, e.nativeEvent.offsetX 

### 클릭
- e.button : 우클릭? 좌클릭?

### 팝업메뉴 contextmenu
- 라이브러리 설치 ```yarn add react-contextmenu```
- ContextMenuTrigger영역에 마우스를 우클릭하면 같은 id의 ContextMenu가 나옴
    - div는 정식 DOM객체 -> 형체 있음
    - ContextMenuTrigger는 형체가 있지 않아서 css 의미가 없음
```js
<ContextMenuTrigger id="abc">
    <div style={{width:100, height:100, border:"black solid 2px",}}></div>
</ContextMenuTrigger>
<ContextMenu id="abc">
    <MenuItem>
        <a href='https://www.naver.com'>네이버로</a>
    </MenuItem>
</ContextMenu>
```

## 팝업 이벤트
