from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def get_cost(self, PriceBuilder): pass
