from abc import ABC, abstractmethod


class Pizza(ABC):
    def __init__(self, weight, sauce):
        self.weight = weight
        self.sauce = sauce

    @abstractmethod
    def cook(self):
        pass
