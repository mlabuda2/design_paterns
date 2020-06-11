from abc import abstractmethod, ABC

from flower_market.flower.flower import Flower


class Rose(Flower, ABC):
    @property
    def name(self) -> str:
        return 'Rose'

    @property
    @abstractmethod
    def color(self): pass
