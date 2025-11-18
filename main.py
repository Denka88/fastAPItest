from urllib import request

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from models.category import Category
from models.categoty_manager import CategoryManager
from models.pizza import Pizza
from models.pizza_manager import PizzaManager

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
pizza_manager = PizzaManager()
category_manager = CategoryManager()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в мир пицц"}

@app.get("/pizzas")
def get_pizzas(request: Request):
    pizzas = pizza_manager.get_all()
    return templates.TemplateResponse("index.html", {"request": request, "pizzas": pizzas})

@app.post("/pizzas/add")
def add_pizza(pizza: Pizza):
    categories = category_manager.get_all()
    return pizza_manager.add_pizza(pizza, categories)

@app.put("/pizzas/edit")
def update_pizza(pizza: Pizza):
    categories = category_manager.get_all()
    return pizza_manager.edit_pizza(pizza.id, pizza.name, pizza.price, pizza.category_id, categories)

@app.delete("/pizzas/delete/{delete_id}")
def delete_pizza(delete_id: int):
    return pizza_manager.delete_pizza(delete_id)

@app.get("/categories")
def get_categories():
    return category_manager.get_all()

@app.post("/categories/add")
def add_category(category: Category):
    return category_manager.add_category(category)

@app.put("/categories/edit")
def update_category(category: Category):
    return category_manager.edit_category(category.id, category.name)

@app.delete("/categories/delete/{delete_id}")
def delete_category(delete_id: int):
    return category_manager.delete_category(delete_id)