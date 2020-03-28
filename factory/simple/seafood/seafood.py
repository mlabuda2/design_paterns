from abc import ABC, abstractmethod


class Seafood(ABC):
    def __init__(self, quantity, sauce):
        self.quantity = quantity
        self.sauce = sauce

    @abstractmethod
    def cook(self):
        pass
