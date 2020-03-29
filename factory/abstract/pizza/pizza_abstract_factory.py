from abc import ABC, abstractmethod

from factory.abstract.food_abstract_factory import FoodFactory
from factory.abstract.pizza.pizza import Pizza


class PizzaFactory(FoodFactory, ABC):

    @abstractmethod
    def cook_double_dough(self, diameter: int, sauce: bool) -> Pizza:
        pass
