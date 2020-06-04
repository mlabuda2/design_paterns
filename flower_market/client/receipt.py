import copy

from flower_market.client.shopping_cart import ShoppingCart


class Receipt:
    def __init__(self, products: list, cost: float) -> None:
        self.products = products
        self.cost = cost

    def copy(self) -> object:
        return copy.deepcopy(self)