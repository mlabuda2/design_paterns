from flower_market.flower.flower_factory import FlowerFactory
from flower_market.flower.rose.red_rose import RedRose
from flower_market.singleton_meta import SingletonMeta


class RedRoseFactory(FlowerFactory, metaclass=SingletonMeta):

    def prepare(self, count: int = 1, artificial: bool = False, cutted: bool = False) -> RedRose:
        return RedRose(count, artificial, cutted)