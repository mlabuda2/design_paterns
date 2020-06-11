from flower_market.client.builders import builder_dispatcher


class ShoppingCart:

    def __init__(self, country: str) -> None:
        self.products = list()
        self.builder = builder_dispatcher[country]

    def __repr__(self):
        product_names = []
        for product in self.products:
            product_names.append(repr(product))
        return f"Shopping cart: {','.join(product_names)}"

    def add(self, product) -> int:
        self.products.append(product)
        return len(self.products)

    def remove(self, product) -> bool:
        if product in self.products:
            self.products.remove(product)
            return True
        return False

    # Facade
    def count(self) -> float:
        sum = 0
        for product in self.products:
            sum += product.get_cost(self.builder)
        return sum

    def clear(self) -> None:
        self.products = list()
