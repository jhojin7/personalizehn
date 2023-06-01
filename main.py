import json
import jinja2
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse 

app = FastAPI(debug=True)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="")

# Step 4: Create the data storage
data = {
    'id': [1, 2, 3,],
    'title': ['Link 1', 'Link 2', 'Link 3'],
    'url': ['https://example.com/1', 'https://example.com/2', 'https://example.com/3'],
    'viewed': [False, False, False],
    'liked': [False, False, False]
}
# df = pd.DataFrame(data)
df = pd.read_csv("posts-2023-06-01.csv")

# Step 5: Define the routes and views
@app.get("/")
def read_links(req: Request):
    # return df.to_dict(orient="records")
    return templates.TemplateResponse("index.html", 
        {"request": req, 
         "links": df.to_dict(orient="records")
         })

@app.get("/data")
def data_itself():
    return json.loads(df.to_json(orient="records"))
    # return JSONResponse(df.to_json(orient="records"))

@app.post("/link/{id}")
def mark_as_viewed(id: int):
    df.loc[df['id'] == id, 'viewed'] = True
    print(df, flush=True)
    df.to_csv("data.csv")
    return {"message": "Link marked as viewed"}

@app.post("/like/{id}")
def mark_as_liked(id: int):
    df.loc[df['id'] == id, 'liked'] = True
    df.to_csv("data.csv")
    return {"message": "Link marked as liked"}

# Step 6: Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True)

