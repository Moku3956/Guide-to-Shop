from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import graph_data
import calculate
from pydantic import BaseModel
from typing import List


app = FastAPI()

#  <link rel="stylesheet" href="../static/map.css">を
#  パースしたときこのエンドポイントにリクエストが送られる
#  それによりstaticディレクトリを探すことができる
app.mount("/static", StaticFiles(directory="static"), name="static")

#  templatesディレクトリを探すことができる
templates = Jinja2Templates(directory="templates")

class RouteRequest(BaseModel):
    lat: float
    lon: float
    currentCordinates: List[str] = []

@app.post("/api/get-route")
def get_info(request_data: RouteRequest):
    lat = request_data.lat
    lon = request_data.lon
    current_cordinates_input = request_data.currentCordinates
    
    node_name = calculate.find_nearest_node(lat, lon, graph_data.nodes, current_cordinates_input)
    route_points_name = calculate.designed_route(node_name)
    # returnで受け取った名前を座標に変換 ↓
    route_points_lat_and_lon = []
    for item in route_points_name:
        route_points_lat_and_lon.append([graph_data.nodes[item]["lat"], graph_data.nodes[item]["lon"]])
    return {
        "route_points_lat_and_lon": route_points_lat_and_lon, # 描画用の座標リスト
        "route_points_name": route_points_name           # JS が次回送るためのノード名前リスト
    }        
@app.get("/")
def display(request: Request):
    # TemplateResponseでレンダリングする
    # requestはまだ理解足りない、docsを見た感じこう書いてた
    return templates.TemplateResponse("map.html", {"request": request})
    

