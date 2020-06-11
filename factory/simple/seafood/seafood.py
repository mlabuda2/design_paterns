from abc import ABC, abstractmethod


class Seafood(ABC):
    def __init__(self, quantity: int, sauce: str):
        self.quantity = quantity
        self.sauce = sauce

    @abstractmethod
    def eat(self):
        pass
