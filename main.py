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
DATAFILE = "data/database1.csv"
df = pd.read_csv(DATAFILE)
print(df, flush=True)


# Step 5: Define the routes and views
@app.get("/")
def index_page(req: Request):
    return templates.TemplateResponse("index.html", {
        "request": req,
        "links": df.to_dict(orient="records"),
    })

@app.post("/click/{id}")
def mark_as_viewed(id: int):
    df.loc[df['id'] == id, 'visited'] = 1
    df.to_csv(DATAFILE)
    return {"message": "Link marked as viewed"}

# @app.post("/like/{id}")
# def mark_as_liked(id: int):
#     df.loc[df['id'] == id, 'liked'] = 1
#     df.to_csv("data.csv")
#     return {"message": "Link marked as liked"}
