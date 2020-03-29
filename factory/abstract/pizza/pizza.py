from abc import ABC, abstractmethod


class Pizza(ABC):
    def __init__(self, diameter: int, sauce: str, double_dough: bool = False):
        self.diameter = diameter
        self.sauce = sauce
        self.double_dough = double_dough

    @abstractmethod
    def eat(self):
        pass

    def get_total_kcal(self):
        return self.diameter * 6
