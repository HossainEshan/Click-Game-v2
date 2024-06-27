from fastapi import FastAPI
from app.api.v1.endpoints import counter
from app.db.init_db import init_db
from app.db.session import SessionLocal, engine

app = FastAPI()

app.include_router(counter.router, prefix="/api/v1/counter", tags=["counter"])

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}