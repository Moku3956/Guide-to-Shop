
const initialLat = 34.981714;
const initialLon = 135.963098;
const initialZoom = 16;

let map = L.map('map').setView([initialLat, initialLon], initialZoom)

const arrowIcon = L.divIcon({
    className: 'arrow-icon-container',
    html: '<div id="direction-arrow">⬆</div>' // マーカーを矢印にする
});

const markerOnDestination = L.marker([34.980316, 135.963133], { color: "red" }).addTo(map); // 店舗の座標に赤いマーク
markerOnDestination.bindPopup("立命館No.1サッカーサークル<br>ぜんざい屋").openPopup()

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map)

// 画面のズームを終えたら、下にあるstartCompassを起動
map.once('zoomend', startCompass);

let currentCordinates = []  // 最短距離のノードが最初に表示された経路内から選ばれるようにする
let markerLayer = null;
let polylinesLayer = null;

async function success(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;

    const url = "/api/get-route"; // POSTメソッドでlat,lonをエンドポイントに渡す
    const request = new Request(url, {
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
            markerLayer.setLatLng([lat, lon]);
        } else {
            markerLayer = L.marker([lat, lon], { icon: arrowIcon }).addTo(map);
        }
        if (polylinesLayer) {
            polylinesLayer.remove();
        }
        polylinesLayer = L.polyline(routeCoordinates.route_points_lat_and_lon, { color: 'blue' }).addTo(map);
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

// success, errorをコールバック
const watchLocation = navigator.geolocation.watchPosition(success, error, options)

// コンパス（ユーザーの方向）機能の追加 ↓

async function startCompass() {
    // requestPermissionがあるかどうかで端末、ブラウザを判別
    // iOSはrequestPermissionで許可を取らなけらばならない
    if (typeof DeviceOrientationEvent.requestPermission === 'function') {
        try {
            const permission = await DeviceOrientationEvent.requestPermission()
            switch (permission) {
                case "granted":
                    window.addEventListener("deviceorientation", handlerForIOS)
                    break
                case "denied":
                    break
                case "default":
                    break
            }
        } catch (error) {
            console.error(`エラー: ${error.name}`)
        }
    } else { //iOS以外は許可を取らなくいい
        window.addEventListener("deviceorientation", handlerForOthers)
    }
}

// iOS用
// iOSはwebkitCompassHeadingが搭載されてる、北が0になる
function handlerForIOS(event) {
    const directionArrow = document.getElementById("direction-arrow")
    if (directionArrow) {
        compass = event.webkitCompassHeading
        directionArrow.style.transform = `rotate(${compass}deg)`
    }
}

// iOS以外用
// その他の端末は、alphaを使う。iOSとの回転方向を合わせた
function handlerForOthers(event) {
    const directionArrow = document.getElementById("direction-arrow")
    if (directionArrow) {
        if (typeof event.alpha !== "number") return;
        compass = 360 - event.alpha
        directionArrow.style.transform = `rotate(${compass}deg)`
    }
}
