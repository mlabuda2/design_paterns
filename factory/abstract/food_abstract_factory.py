from abc import ABC, abstractmethod

from factory.abstract.singleton_meta import SingletonMeta


class FoodFactory(ABC, metaclass=SingletonMeta):

    @abstractmethod
    def cook(self): pass