from fastapi import FastAPI
from starlette.templating import Jinja2Templates

from models.pizza import Pizza
from models.manager import PizzaManager

app = FastAPI()
pizza_manager = PizzaManager()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в мир пицц"}

@app.get("/pizzas")
def get_pizzas():
    return pizza_manager.get_all()

@app.post("/pizzas/add")
def add_pizza(pizza: Pizza):
    return pizza_manager.add_pizza(pizza)

@app.put("/pizzas/edit")
def update_pizza(pizza: Pizza):
    return pizza_manager.edit_pizza(pizza.id, pizza.name, pizza.price)

@app.delete("/pizzas/delete/{delete_id}")
def delete_pizza(delete_id: int):
    return pizza_manager.delete_pizza(delete_id)