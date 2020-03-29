from abc import ABC, abstractmethod


class Seafood(ABC):
    def __init__(self, quantity: int, sauce: str, raw: bool = False):
        self.quantity = quantity
        self.sauce = sauce
        self.raw = raw

    @abstractmethod
    def eat(self):
        pass

    def get_total_kcal(self):
        return self.quantity * 100
