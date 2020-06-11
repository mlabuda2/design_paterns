from abc import ABC, abstractmethod

from flower_market.singleton_meta import SingletonMeta


class FlowerFactory(ABC, metaclass=SingletonMeta):

    @abstractmethod
    def prepare(self, count, artificial, cutted): pass