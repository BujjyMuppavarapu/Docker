from fastapi import FastAPI
from app import ping

app = FastAPI()

app.include_router(ping.router)