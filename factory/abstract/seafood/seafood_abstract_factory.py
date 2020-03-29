from abc import ABC, abstractmethod

from factory.abstract.food_abstract_factory import FoodFactory
from factory.abstract.seafood.seafood import Seafood


class SeafoodFactory(FoodFactory, ABC):

    @abstractmethod
    def serve_raw(self, quantity: int, sauce: str) -> Seafood:
        pass
