from typing import List

from flower_market.client.receipt import Receipt
from flower_market.client.shopping_cart import ShoppingCart


class Client:
    def __init__(self, name: str, money: float, country: str) -> None:
        self.name = name
        self.money = money
        self.country = country
        self.shopping_cart = ShoppingCart(country)
        self.purchase_history = list()

    def get(self, product: object) -> None:
        self.shopping_cart.add(product)
        print(f"{product} added to {self.name}'s shopping cart.")

    def get_all(self, products: List[object]) -> None:
        for product in products:
            self.shopping_cart.add(product)

    def get_shopping_cart(self) -> ShoppingCart:
        return self.shopping_cart

    def takeout_shopping_cart(self) -> List[object]:
        products = list(self.shopping_cart.products)
        self.shopping_cart.clear()
        return products

    def pay(self) -> bool:
        cost = self.shopping_cart.count()
        if self.money >= cost:
            self.money -= cost
            self.purchase_history.append(Receipt(self.shopping_cart.products, cost))
            self.shopping_cart.clear()
            print(f"{self.name} paying {cost}: Success!")
            return True
        print(f"{self.name} paying {cost}: Not enough money!")
        return False

    def get_cash(self) -> float:
        return self.money

    def get_purchase_history(self, count: int) -> list:
        if count >= len(self.purchase_history):
            return self.purchase_history
        else:
            return self.purchase_history[-count:]
