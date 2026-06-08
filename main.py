from fastapi import FastAPI
import random

app = FastAPI()

quotes = [
    "Success comes from consistency.",
    "Keep learning every day.",
    "Believe in yourself."
]

@app.get("/")
def home():
    return {"message": "Hello"}

@app.get("/quote")
def get_quote():
    return {"quote": random.choice(quotes)}