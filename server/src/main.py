from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:4173",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return "Dockerize Sample Application"

@app.get("/ping")
def ping():
    return f"pong { random.randrange(1, 100, 1) }"