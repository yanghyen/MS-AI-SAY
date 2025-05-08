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

function searchKeyword(){
    $("#search").keyup(function (e) {
        if (e.keyCode == 13) {
            var search2Txt = $(this).val();
            $.ajax({
                url: "https://dapi.kakao.com/v2/local/search/keyword.json",
                data: { query: search2Txt, radius: 100, y: map.getCenter().getLat(), x: map.getCenter().getLng() },
                beforeSend: function (req) {
                    req.setRequestHeader("Authorization", "KakaoAK 48412524e1d7ccbf166a18a4687b943e")
                },
                success: function (search2Data) {
                    $("#resultArea").empty();
                    $.each(search2Data.documents, function (i, l) {
                        var nameTd = $("<td></td>").text(l.place_name);
                        var likeButton = $("<button></button>").text("❤");
                        var addrTd = $("<td></td>").text(l.road_address_name);
                        var phoneTd = $("<td></td>").attr("align", "right").text(l.phone);
                        var tr1 = $("<tr></tr>").append(nameTd, likeButton);
                        var tr2 = $("<tr></tr>").append(addrTd)
                        var tr3 = $("<tr></tr>").append(phoneTd);
                        var table = $("<table></table>").attr("class", "l")
                            .attr("onclick", "moveMap(" + l.y + "," + l.x + ");").append(tr1, tr2, tr3);
                        $("#resultArea").append(table);
    
                    });
                }
            })
        }
    
    });
};

function getPlaceData() {
    $.getJSON("http://195.168.9.206:5255/place.get", function (json) {
        $("ul").empty();
        $.each(json.places, function(i, p){
            var br1 = $("<br>");
            var br2 = $("<br>");
            var li = $("<li></li>").append(p.name_eng, br1, p.name_kor, br2);
            $("ul").append(li);
        });
        $("ul").listview("refresh");
        // 페이지 pageCount DAO 만들고 하기 
        // $("#pageControlArea td").empty();
        // for (var i = 1; i <= json.pageCount; i++) {
        //     var a = $("<a></a>").attr("href", "").text(i);
        //     $("#pageControlArea td").append(a);
        // }
    });
};

$(function () {
    // main에선 이렇게 호출만 하기
    getCurrentLocation();   
    searchKeyword();
    getPlaceData();
});


