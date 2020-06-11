from abc import ABC, abstractmethod

from factory.abstract.food_abstract_factory import FoodFactory
from factory.abstract.seafood.seafood import Seafood
from factory.abstract.singleton_meta import SingletonMeta


class SeafoodFactory(FoodFactory, ABC, metaclass=SingletonMeta):

    @abstractmethod
    def serve_raw(self, quantity: int, sauce: str) -> Seafood:
        pass
