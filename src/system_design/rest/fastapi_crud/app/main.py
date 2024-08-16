from fastapi import FastAPI
from .routers import recipes_router


app = FastAPI()
app.include_router(recipes_router.router)


@app.get("/")
async def read_main():
    return {'msg': 'Hello World'}
