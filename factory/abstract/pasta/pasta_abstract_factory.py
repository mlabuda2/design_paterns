from abc import abstractmethod, ABC

from factory.abstract.food_abstract_factory import FoodFactory
from factory.abstract.pasta.pasta import Pasta
from factory.abstract.singleton_meta import SingletonMeta


class PastaFactory(FoodFactory, ABC, metaclass=SingletonMeta):

    @abstractmethod
    def cook_al_dente(self, weight: int, parmesan: bool) -> Pasta:
        pass
