from abc import ABC, abstractmethod


class FoodFactory(ABC):

    @abstractmethod
    def cook(self): pass