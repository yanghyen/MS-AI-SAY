# Wel Korea : 외국인을 위한 지도 앱 프로젝트

한국에 거주하거나 방문한 외국인을 위한 지도 앱입니다. 영어로 검색하고, 장소를 찾고, 경로를 안내받고, 즐겨찾기까지 가능한 필수 생활 도우미 앱을 목표로 합니다.

---

## ✅ 추천 MVP 개발 순서

### 1. 📍 현재 위치 기반 지도 표시

- Geolocation API 사용해 현재 위치 표시
- 마커 및 맵 중심 설정

```javascript
navigator.geolocation.getCurrentPosition(function (position) {
    const lat = position.coords.latitude;
    const lng = position.coords.longitude;
    const center = new kakao.maps.LatLng(lat, lng);
    map.setCenter(center);
    marker.setPosition(center);
});
```

---

### 2. 🔍 영어 키워드 검색 → 한글 번역 → 장소 검색

**목표**: 사용자가 입력한 영어 키워드를 한글로 번역하여, 해당 키워드로 한국의 장소를 검색합니다.

1. 영어로 입력된 검색어 -> 그대로 카카오맵에 검색
    - 예: ```keywordSearch("Kkua")```
    - 어떤 상호명은 영문 등록도 되어 있어 바로 검색 가능
2. 결과 없으면 번역 사용자가 입력한 영어 키워드를 FastAPI를 통해 Papago API로 번역
    - 예: ```Kkua``` → ```꾸아``` → ```keywordSearch("꾸아")```
    - 번역된 한글 키워드를 기반으로 Naver 지도 API에서 장소를 검색

```python
# FastAPI에서 번역 처리 예시
@app.get("/search")
async def search(query: str):
    translated_query = translate_english_to_korean(query)
    search_results = naver_map_search(translated_query)
    return search_results
```
```javascript
function searchKeyword(text) {
    searchWithKakao(text, function(results) {
        if (results.length === 0) {
            // 결과 없으면 서버에 영어 → 한글 번역 요청
            $.get("/translate", { q: text }, function(translated) {
                searchWithKakao(translated, showResults);
            });
        } else {
            showResults(results);
        }
    });
}
```

---

### 3. 📄 검색 결과 표시 + 지도 마커

**목표**: 검색된 장소의 정보를 지도에 표시하고, 클릭 시 해당 위치로 이동합니다.

**기능**:
- 검색된 장소를 영어로 번역하여 리스트에 표시
- 리스트 항목 클릭 시 지도 이동 및 마커 표시

```javascript
searchResults.forEach(result => {
    const listItem = document.createElement('li');
    listItem.textContent = result.name;  // 영어로 표시
    listItem.addEventListener('click', function() {
        var ll = new kakao.maps.LatLng(result.latitude, result.longitude);
        map.setCenter(ll);
        marker.setPosition(ll);
    });
    document.getElementById("resultList").appendChild(listItem);
});
```

---

### 4. 🛣️ 경로 안내 기능 추가 (도보/자동차)

**목표**: 사용자가 목적지까지 도보나 자동차로 경로를 안내합니다.

**기능**:
- 출발지/도착지를 FastAPI에 보내 Naver Directions API 호출
- 반환된 경로를 지도에 polyline으로 표시

```python
@app.get("/directions")
async def get_directions(start_lat: float, start_lng: float, end_lat: float, end_lng: float):
    directions = naver_directions_api(start_lat, start_lng, end_lat, end_lng)
    return directions
```

```javascript
directions.routes[0].legs[0].steps.forEach(function(step) {
    var path = step.polyline.points;
    var polyline = new kakao.maps.Polyline({
        path: path,
        strokeColor: "#FF0000", 
        strokeWeight: 3
    });
    polyline.setMap(map);
});
```

---

### 5. 💾 즐겨찾기 저장 기능 (OracleDB 연동)

**목표**: 사용자가 관심 장소를 즐겨찾기로 저장하고, 나중에 다시 볼 수 있도록 합니다.

**기능**:
- 장소 저장 버튼 클릭 시 FastAPI로 POST 요청
- OracleDB에 저장, 사용자별 리스트 제공

```python
@app.post("/favorite")
async def save_favorite(place_id: int, user_id: int):
    save_to_db(place_id, user_id)
    return {"message": "즐겨찾기 저장 완료"}
```

---

### 6. 💬 영어 → 한글 번역 및 검색 시 오류 처리

**목표**: 영어 검색어로 검색이 되지 않을 경우, 자동 번역하여 재검색합니다.

**기능**:
- 영어 키워드를 바로 검색
- 검색 결과가 없으면 Papago로 번역 후 재검색

```javascript
keywordSearch("Kkua")
.then(response => {
    if (!response.results.length) {
        translateToKorean("Kkua")
        .then(translated => {
            keywordSearch(translated);
        });
    }
});
```

---

### 💡 팁: 로컬 캐시 활용

자주 번역하는 키워드는 OracleDB에 캐싱해두면 API 요금도 줄이고 속도도 개선할 수 있습니다.  
(이때 발음대로 입력한 것과 의미대로 입력한 것 구분해서 번역해야 함!)

```sql
SELECT korean FROM translation_cache WHERE english = 'kkua';
```

---

## 📈 확장 가능성

이 프로젝트는 외국인을 위한 다양한 기능을 제공하는 지도 앱으로 확장 가능성이 큽니다:

- **다국어 지원 확대**: 영어 외에 중국어, 일본어 등도 번역 및 검색 지원
- **음성 안내 기능**: 경로 안내 시 음성으로 길 안내 제공
- **지역 기반 추천 서비스**: 관심 카테고리(식당, 병원 등)에 대한 지역 추천 기능
- **소셜 기능**: 장소 리뷰, 평점, 사진 업로드 기능
- **통합 예약 시스템**: 병원/식당 등 예약 가능한 장소와 연동

---

## 📁 기술 스택

- **Backend**: FastAPI
- **Frontend**: jQuery Mobile, HTML, CSS, JS
- **Database**: OracleDB
- **지도**: Kakao Maps JS SDK
- **번역**: Naver Papago API (또는 Google Translate API)
