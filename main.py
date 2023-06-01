import json
import jinja2
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse 

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="")

# Step 4: Create the data storage

# df = pd.DataFrame(data)
df = pd.read_csv("data.csv")

# Step 5: Define the routes and views
@app.get("/")
def index_page(req: Request):
    return templates.TemplateResponse("index.html", {
        "request": req,
        "links": df.to_dict(orient="records"),
        "dropdown_options": list(set(df["date"])),
    })

@app.get("/data")
def data_itself():
    return json.loads(df.to_json(orient="records"))
    # return JSONResponse(df.to_json(orient="records"))

@app.post("/link/{id}")
def mark_as_viewed(id: int):
    df.loc[df['id'] == id, 'viewed'] = 1
    df.to_csv("data.csv")
    return {"message": "Link marked as viewed"}

@app.post("/like/{id}")
def mark_as_liked(id: int):
    df.loc[df['id'] == id, 'liked'] = 1
    df.to_csv("data.csv")
    return {"message": "Link marked as liked"}
