import copy


class Receipt:
    def __init__(self, products: list, cost: float) -> None:
        self.products = products
        self.cost = cost

    # Prototype
    def copy(self) -> object:
        return copy.deepcopy(self)