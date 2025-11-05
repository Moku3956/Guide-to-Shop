
async function success(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    
    // GETメソッドでlat,lonをエンドポイントに渡す
    const url = `/api/get-route?lat=${lat}&lon=${lon}`;
    const request = new Request(url);

    try {
        const response = await fetch(request);
        if (!response.ok) {
            throw new Error(`レスポンスステータス: ${response.status}`);
        }
        // calculate.pyで計算した結果を受け取る
        const currentLocation = await response.json() 

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









