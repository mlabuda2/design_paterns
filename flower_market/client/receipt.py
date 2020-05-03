import copy

from flower_market.client.shopping_cart import ShoppingCart


class Receipt:
    def __init__(self, products: list, cost: int) -> None:
        self.products = products
        self.cost = cost

    def copy(self):
        return copy.deepcopy(self)