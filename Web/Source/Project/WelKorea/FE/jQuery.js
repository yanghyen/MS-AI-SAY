var map; var marker; var mapArea;
var rvArea; var rvManager; var roadview;

function moveMap(lat, lng) {
    var ll = new kakao.maps.LatLng(lat, lng);
    map.setCenter(ll);
    marker.setPosition(ll);
    rvManager.getNearestPanoId(ll, 100, function (panoId) {
        roadview.setPanoId(panoId, ll);
    }); //로드뷰 객체
}

function getCurrentLocation(){
    mapArea = document.getElementById('map');
    rvArea = document.getElementById('rv'); //로드뷰를 표시할 div
    rvManager = new kakao.maps.RoadviewClient(); //좌표로부터 로드뷰 파노ID를 가져올 로드뷰 helper객체
    roadview = new kakao.maps.Roadview(rvArea);
    
    navigator.geolocation.getCurrentPosition(function (addr) {
        var lat = addr.coords.latitude;
        var lng = addr.coords.longitude;
        var ll = new kakao.maps.LatLng(lat, lng);
        map = new kakao.maps.Map(mapArea, {
            center: ll,
            level: 3
        });
        marker = new kakao.maps.Marker({
            map: map,
            position: ll
        });
        moveMap(lat, lng);
    });
};

function searchKeyword() {
    $("#search").on("keyup", function (e) {
        if (e.keyCode === 13) {
            const search2Txt = $(this).val();

            $.ajax({
                url: "https://dapi.kakao.com/v2/local/search/keyword.json",
                data: {
                    query: search2Txt,
                    radius: 100,
                    y: map.getCenter().getLat(),
                    x: map.getCenter().getLng()
                },
                beforeSend: function (req) {
                    req.setRequestHeader("Authorization", "KakaoAK 48412524e1d7ccbf166a18a4687b943e");
                },
                success: function (search2Data) {
                    $("#resultArea").empty();

                    $.each(search2Data.documents, function (i, place) {
                        const resultCard = $("<div></div>")
                            .css({
                                border: "1px solid #ccc",
                                padding: "10px",
                                marginBottom: "10px",
                                borderRadius: "8px",
                                cursor: "pointer"
                            })
                            .append(`
                                <div style="font-weight: bold;">
                                    ${place.place_name} <button style="float:right;">❤</button>
                                </div>
                                <div>${place.road_address_name || place.address_name}</div>
                                <div style="text-align: right; font-size: 0.9em; color: #555;">
                                    ${place.phone || ''}
                                </div>
                            `)
                            .on("click", function () {
                                moveMap(place.y, place.x);
                            });

                        $("#resultArea").append(resultCard);
                    });
                },
                error: function (xhr, status, error) {
                    console.error("API 요청 오류:", error);
                }
            });
        }
    });
}




function getPlaceData(page) {
    $.getJSON("http://195.168.9.206:5255/place100.get?page=" + page, function (json) {
        $("#placeList").empty();
        $.each(json.places, function(i, p){
            var br1 = $("<br>");
            var br2 = $("<br>");
            var li = $("<li></li>").append(p.name_eng, br1, p.name_kor, br2);
            $("#placeList").append(li);
        });
        $("placeList").listview("refresh");
        // 페이지 pageCount DAO 만들고 하기 
        $("#pageControlArea td").empty();
        for (var i = 1; i <= json.pageCount; i++) {
            var a = $("<a></a>").attr("href", "").text(i);
            $("#pageControlArea td").append(a);
        }
    });
};

function regPlaceData() {
    $("#place_input_btn").click(function () {
        let nn = $("#place_name_input").val();
        let dd = $("#place_desc_input").val();

        let url = "http://195.168.9.206:5255/place100.reg?name=" + nn +"&desc=" + dd;
        $.getJSON(url, function (json) {
        });
        
    });
}


$(function () {
    // main에선 이렇게 호출만 하기
    getCurrentLocation();   
    searchKeyword();
    getPlaceData(1);
    regPlaceData();
});


