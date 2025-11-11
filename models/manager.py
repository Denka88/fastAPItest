from models.pizza import Pizza

class PizzaManager:
    def __init__(self):
        self.pizzas = []

    def get_all(self):
        return self.pizzas

    def add_pizza(self, pizza: Pizza) -> Pizza:
        self.pizzas.append(pizza)
        return pizza