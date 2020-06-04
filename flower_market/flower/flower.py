from abc import ABC, abstractmethod

from flower_market.price_list.price_list import PriceList


class Flower(ABC):
    def __init__(self, count: int = 1, artificial: bool = False, cutted: bool = False) -> None:
        self.count = count
        self.artificial = artificial
        self.cutted = cutted

    def __repr__(self):
        return self.name + ' x' + str(self.count)

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def margin(self) -> float:
        pass

    def get_cost(self, PriceBuilder) -> float:  # Facade
        price = PriceList().get_price(self, PriceBuilder)
        return price.gross * self.count

    def get_cost_for_wholesale(self, PriceBuilder) -> float:  # Facade
        price = PriceList().get_price(self, PriceBuilder)
        return price.net * self.count
