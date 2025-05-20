import React from 'react'
import {ContextMenu, ContextMenuTrigger, MenuItem} from "react-contextmenu"
 
const MyPopupMenu = () => {
    // ContextMenuTrigger영역에 마우스를 우클릭하면
    // 같은 id의 ContextMenu가 나옴
  return (
    <>
        <ContextMenuTrigger id="abc">
            <div style={{width:100, height:100, border:"black solid 2px",}}></div>
        </ContextMenuTrigger>
        <ContextMenu id="abc">
            <MenuItem>
                <a href='https://www.naver.com'>네이버로</a>
            </MenuItem>
        </ContextMenu>
    </>
  )
}

export default MyPopupMenu