from fastapi import FastAPI
from util.objects import Update, LastUpdate

app = FastAPI()

@app.get("/start/", status_code=201)
async def start() -> Update:
   return Update()

@app.get("/end/", status_code=200)
async def end() -> Update:
   return Update()

@app.get("/update/", status_code=200)
async def update(item: LastUpdate) -> Update:
   return Update()