from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Cors
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def welcome():
    return {"Bad request": "use /api/ na rota"}

@app.get("/api/")
def welcome_api():
    return {"Bem": "Vindo"}

@app.get("/api/name/{name}")
def welcome_someone(name: str):
    return {"Bem-vindo": name}
