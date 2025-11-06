
const initialLat = 34.981714;
const initialLon = 135.963098;
const initialZoom = 16;


let map = L.map('map').setView([initialLat, initialLon], initialZoom)
const markerOnDestination = L.marker([34.980316, 135.963133], {color: "red"}).addTo(map); // 店舗の座標に赤いマーク
markerOnDestination.bindPopup("立命館No.1サッカーサークル<br>ぜんざい屋").openPopup()

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map)

let currentCordinates = []
let markerLayer = null;
let polylinesLayer = null;

async function success(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    // GETメソッドでlat,lonをエンドポイントに渡す
    const url = "/api/get-route";
    const request = new Request(url,{
        method: "POST",
        body: JSON.stringify({
            "lat": lat,
            "lon": lon,
            "currentCordinates": currentCordinates
        }),
        headers: {
            'Content-Type': 'application/json' 
        }
    });

    try {
        const response = await fetch(request);
        if (!response.ok) {
            throw new Error(`レスポンスステータス: ${response.status}`);
        }
        // calculate.pyで計算した結果を受け取る,経路の座標リスト
        const routeCoordinates = await response.json()
        if (markerLayer) {
            markerLayer.remove();
        }
        if (polylinesLayer) {
            polylinesLayer.remove();
        }
        markerLayer = L.marker([lat, lon]).addTo(map);
        polylinesLayer = L.polyline(routeCoordinates.route_points_lat_and_lon, {color: 'blue'}).addTo(map);
        currentCordinates = routeCoordinates.route_points_name;
    } catch (error) {
        console.error("エラー:", error);
    }
}


//エラー処理
function error(error) {

    console.warn(`ERROR(${error.code}): ${error.message}`);

    switch (error.code) {
        case error.PERMISSION_DENIED:
            alert("位置情報の利用が許可されていません");
            break
        case error.POSITION_UNAVAILABLE:
            alert("位置情報を取得できませんでした");
            break
        case error.TIMEOUT:
            alert("位置情報の取得がタイムアウトしました");
            break
        default:
            alert("不明なエラーが発生しました")
            break
    }
}

// maximumAgeを0にすることで位置情報をキャッシュしない
const options = {
    enableHighAccuracy: true,
    maximumAge: 0,
    timeout: 5000,
};

// success, errorをコールバックする
const watchLocation = navigator.geolocation.watchPosition(success, error, options)



