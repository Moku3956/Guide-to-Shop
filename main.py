from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import graph_data

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/api/get-route")
def get_info(lat: float, lon: float):
    print(f"{lat}, {lon}")
    
@app.get("/")
def display(request: Request):
    return templates.TemplateResponse("map.html", {"request": request})
    

