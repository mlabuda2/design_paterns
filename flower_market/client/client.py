from flower_market.client.receipt import Receipt
from flower_market.client.shopping_cart import ShoppingCart


class Client:
    def __init__(self, name: str, money: float, country: str) -> None:
        self.name = name
        self.money = money
        self.country = country
        self.shopping_cart = ShoppingCart(country)
        self.purchase_history = list()

    def get(self, product):
        self.shopping_cart.add(product)

    def get_all(self, products):
        for product in products:
            self.shopping_cart.add(product)

    def get_shopping_cart(self):
        return self.shopping_cart

    def takeout_shopping_cart(self):
        products = list(self.shopping_cart.products)  # TODO sprawdzic czy działa
        self.shopping_cart.clear()
        return products

    def pay(self):
        cost = self.shopping_cart.count()
        if self.money >= cost:
            self.money -= cost
            self.purchase_history.append(Receipt(self.shopping_cart.products, cost))
            self.shopping_cart.clear()
            return True
        return False

    def get_cash(self):
        return self.money

    # def order(self):
    #     pass

    def get_purchase_history(self, count):
        if count >= len(self.purchase_history):
            return self.purchase_history
        else:
            return self.purchase_history[-count:]
