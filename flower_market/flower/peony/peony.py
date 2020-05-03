from abc import abstractmethod, ABC

from flower_market.flower.flower import Flower


class Peony(Flower, ABC):
    @property
    def name(self):
        return 'Peony'

    @property
    @abstractmethod
    def color(self): pass
