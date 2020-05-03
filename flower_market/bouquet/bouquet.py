import copy

from flower_market.price_list.price_list import PriceList


class Bouquet:
    def __init__(self, flowers) -> None:
        self.flowers = flowers

    def add(self, flower) -> None:
        self.flowers.append(flower)

    def get_cost(self, PriceBuilder) -> float:  # Facade
        sum = 0
        for flower in self.flowers:
            sum += PriceList().get_price(flower, PriceBuilder).gross * flower.count
        sum = sum * 1.2
        return sum

    def copy(self):
        return copy.deepcopy(self)
