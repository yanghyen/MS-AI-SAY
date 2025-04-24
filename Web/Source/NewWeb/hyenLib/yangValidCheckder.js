// JavaScript 유효성검사 라이브러리
// - 다양한 상황에 대응가능하게 최대한 일반적으로 제작
// - 부정적인 컨셉

// <input> 넣었을때
// 안썼으면 true, 썼으면 false
function isEmpty(field) {
    return !field.value;
}

// <input>, 최소글자수 넣었을때
// 짧으면 true, 안짧으면 false
function lessThan(field, len) {
    return field.value.length < len;
}

// <input> 넣었을때
// 한글, 특수문자, 한자, 일본어 들어있으면 true, 아니면 false
// -> 영어, 숫자, -_.@가 아닌게 들어있으면 true, 그걸로만 구성되어있으면 false
function containsHS(field) {
    var set = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-_@.";
    for (var i = 0; i < field.value.length; i++) {
        if (set.indexOf(field.value[i]) == -1) {
            return true;
        }
    }
    return false;
}

// <input> x 2 넣었을때
// 다르면 true
function notEqual(field1, field2) {
    return field1.value != field2.value;
}

// <input>, 문자열세트를 넣었을때
// 그게 안들어있으면 true
function notContains(field, set) {
    for (var i = 0; i < set.length; i++) {
        if (field.value.indexOf(set[i]) != -1) {
            return false;
        }
    }
    return true;
}

// <input> 넣었을때
// 숫자가 아니면 true
function isNotNum(field) {
    return isNaN(field.value) || (field.value.indexOf(" ") != -1);
}

// 파일검사
    // 다른 거 : field.value 거기다 쓴 글자
    // 파일타입 :  field.value는 선택한 파일명이 글자로 저장됨
    // 파일명만 체크?
    // 1) JS에서 전문적으로 파일 체크 불가
    // 2) 유효성 검사는 사용자 위해서 

// <input>, 확장자 넣었을 때 
// 그 파일이 아니면 true
// isNotType(psaField, "png")
function isNotType(field, type) {
    type = "." + type;
    return field.value.toLowerCase().indexOf(type) == -1;
}