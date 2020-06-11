from abc import ABC, abstractmethod

from factory.abstract.food_abstract_factory import FoodFactory
from factory.abstract.pizza.pizza import Pizza
from factory.abstract.singleton_meta import SingletonMeta


class PizzaFactory(FoodFactory, ABC, metaclass=SingletonMeta):

    @abstractmethod
    def cook_double_dough(self, diameter: int, sauce: bool) -> Pizza:
        pass
