from abc import ABC, abstractmethod


class Pizza(ABC):
    def __init__(self, diameter: int, sauce: str):
        self.diameter = diameter
        self.sauce = sauce

    @abstractmethod
    def eat(self):
        pass
