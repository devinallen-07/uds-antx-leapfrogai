from fastapi import FastAPI
from objects import Update, LastUpdate

app = FastAPI()

@app.get("/start/", status_code=201)
async def start():
   return {'event_id':1}

@app.get("/end/", status_code=204)
def end():
   return None

@app.get("/update/", status_code=200)
def update(item: LastUpdate) -> Update:
   return Update()