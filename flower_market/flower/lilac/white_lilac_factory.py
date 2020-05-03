from flower_market.flower.flower_factory import FlowerFactory
from flower_market.flower.lilac.white_lilac import WhiteLilac
from flower_market.singleton_meta import SingletonMeta


class WhiteLilacFactory(FlowerFactory, metaclass=SingletonMeta):

    def prepare(self, count: int = 1, artificial: bool = False, cutted: bool = False):
        return WhiteLilac(count, artificial, cutted)