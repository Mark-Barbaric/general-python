from fastapi import FastAPI
from .routers import items_router

app = FastAPI()
app.include_router(items_router.router)

@app.get("/")
async def read_main():
    return {'msg': 'Hello World'}