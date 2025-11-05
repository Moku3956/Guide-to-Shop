from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import graph_data
import calculate

app = FastAPI()

#  <link rel="stylesheet" href="../static/map.css">を
#  パースしたときこのエンドポイントにリクエストが送られる
#  それによりstaticディレクトリを探すことができる
app.mount("/static", StaticFiles(directory="static"), name="static")

#  templatesディレクトリを探すことができる
templates = Jinja2Templates(directory="templates")

@app.get("/api/get-route")
def get_info(lat: float, lon: float):
    node_name = calculate.find_nearest_node(lat, lon, graph_data.nodes)
    return calculate.designed_route(node_name)
    
@app.get("/")
def display(request: Request):
    # TemplateResponseでレンダリングする
    return templates.TemplateResponse("map.html", {"request": request})
    

