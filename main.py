from typing import Optional
from urllib import request

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette import status
from starlette.responses import RedirectResponse

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
    categories = category_manager.get_all()
    return templates.TemplateResponse("index.html", {"request": request, "pizzas": pizzas, "categories": categories})

@app.post("/pizzas/add")
def add_pizza(
        name: str = Form(...),
        price: float = Form(...),
        category_id: Optional[int] = Form(...),
):
    categories = category_manager.get_all()
    pizza = Pizza(name=name, price=price, category_id=category_id)
    result = pizza_manager.add_pizza(pizza, categories)
    if result.get("message") == "Пицца успешно добавлена":
        return RedirectResponse(url="/pizzas", status_code=status.HTTP_303_SEE_OTHER)
    else:
        return result

@app.put("/pizzas/edit")
def update_pizza(pizza: Pizza):
    categories = category_manager.get_all()
    return pizza_manager.edit_pizza(pizza.id, pizza.name, pizza.price, pizza.category_id, categories)

@app.delete("/pizzas/delete/{delete_id}")
def delete_pizza(delete_id: int):
    return pizza_manager.delete_pizza(delete_id)

@app.get("/categories")
def get_categories(request: Request):
    categories = category_manager.get_all()
    return templates.TemplateResponse("categories.html", {"request": request, "categories": categories})

@app.post("/categories/add")
def add_category(
        name: str = Form(...),
):
    category = Category(name=name)
    result = category_manager.add_category(category)
    if result.get("message") == "Категория успешно добавлена":
        return RedirectResponse(url="/categories", status_code=status.HTTP_303_SEE_OTHER)
    else:
        return result

@app.get("/categories/edit/{category_id}")
def get_categories(request: Request):
    category = category_manager.get_by_id(category_id=request.query_params.get("category_id"))
    return templates.TemplateResponse("edit_category.html", {"request": request, "categories": categories})

@app.put("/categories/edit")
def update_category(
        id: Optional[int] = Form(...),
        name: str = Form(...),
):
    edited_category = category_manager.edit_category(id, name)
    if edited_category.get("message") == f"Категория с идентификатором {id} успешно обновлена":
        return RedirectResponse(url="/categories", status_code=status.HTTP_303_SEE_OTHER)
    else:
        return edited_category

@app.delete("/categories/delete/{delete_id}")
def delete_category(delete_id: int):
    return category_manager.delete_category(delete_id)