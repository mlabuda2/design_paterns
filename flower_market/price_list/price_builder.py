from abc import ABC, abstractmethod

from builder.simple_builder.vpc import VPC
from flower_market.price_list.price import Price


class PriceBuilder(ABC):
    def __init__(self, base_price: float, margin: float):
        self.price = Price()
        self.price._base = base_price
        self.price._margin = margin

    @property
    @abstractmethod
    def tax(self) -> int:
        pass

    @abstractmethod
    def add_export_cost(self):
        pass

    @abstractmethod
    def set_net(self):
        pass

    @abstractmethod
    def set_gross(self):
        pass

    @abstractmethod
    def set_tare(self):
        pass