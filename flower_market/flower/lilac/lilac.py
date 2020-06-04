from abc import abstractmethod, ABC

from flower_market.flower.flower import Flower


class Lilac(Flower, ABC):
    @property
    def name(self) -> str:
        return 'Lilac'

    @property
    @abstractmethod
    def color(self): pass
