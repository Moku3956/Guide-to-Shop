# Guide-to-Shop
## 概要
学祭で利用するWebアプリケーションです。 ユーザーの現在地を取得し、大学構内の地図上にサークルの店舗への経路を表示します。

## 主な機能
現在地の表示: 端末の位置情報（Geolocation API）を使い、OpenStreetMap上に現在の位置を↓で表示します。
画面をクリック、タップすると端末が向いている方角が分かります！

### 経路検索と表示:

graph_data.py で定義されたキャンパス内のノード（地点）とエッジ（道順）に基づいています。

ユーザーの現在地に最も近いノードを自動的に計算します（calculate.pyのfind_nearest_node）。

最も近いノードから目的地（"goal"）までの定義済みルートをgraph_data.edges から抽出し、地図上に青いポリラインで描画します。

リアルタイム更新: watchPosition を使用しており、ユーザーが移動すると位置情報と経路が自動で更新されます。

## 技術スタック
### バックエンド:

Python 3

FastAPI: APIサーバーの構築

Uvicorn: ASGIサーバー

Haversine: 2点間の距離計算

Jinja2: HTMLテンプレートのレンダリング

### フロントエンド:

HTML

CSS

JavaScript (ES6)

### マップ:

Leaflet.js: インタラクティブマップライブラリ

OpenStreetMap: タイルマップ

### 開発環境:

VS Code Dev Containers

