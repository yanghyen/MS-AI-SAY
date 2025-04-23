function check() {
    // 왜 이 값들을 이 위치에 썼을까?
    // 정리 차원
    var nameField = document.joinForm.name;
    var heightField = document.joinForm.height;
    var weightField = document.joinForm.weight;
    var psaField = document.joinForm.psa;

    if (isEmpty(nameField)) {
        alert("이름?");
        nameField.value = "";
        nameField.focus();
        return false;
    }
    if (isEmpty(heightField) || isNotNum(heightField)) {
        alert("키는?");
        heightField.value = "";
        heightField.focus();
        return false;
    }
    if (isEmpty(weightField) || isNotNum(weightField)) {
        alert("키는?");
        weightField.value = "";
        weightField.focus();
        return false;
    }
    if (
        isEmpty(psaField)
        ||
        (
            isNotType(psaField, "jpg") &&
            isNotType(psaField, "png") &&
            isNotType(psaField, "gif") &&
            isNotType(psaField, "bmp") 
        )
    ) {
        alert("프사?");
        return false; 
    }
    return true;
}
