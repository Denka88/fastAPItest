from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в мир пицц"}

@app.get("/pizzas")
def get_pizzas():
    return {"pizzas": ["Маргарита", "Пепперони", "Гавайская"]}