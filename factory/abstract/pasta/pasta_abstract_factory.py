from abc import abstractmethod, ABC

from factory.abstract.food_abstract_factory import FoodFactory
from factory.abstract.pasta.pasta import Pasta


class PastaFactory(FoodFactory, ABC):

    @abstractmethod
    def cook_al_dente(self, weight: int, parmesan: bool) -> Pasta:
        pass
