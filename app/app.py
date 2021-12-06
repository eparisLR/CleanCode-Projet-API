from fastapi import FastAPI
from .routers.token_router import router as TokenRouter

app = FastAPI()

app.include_router(TokenRouter, tags=["Token"])

@app.get("/", tags=["API Root"])
async def read_root():
    return {"message": "Welcome to TokenAPI"}
