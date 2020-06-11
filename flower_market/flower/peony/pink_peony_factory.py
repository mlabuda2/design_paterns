from flower_market.flower.flower_factory import FlowerFactory
from flower_market.flower.peony.pink_peony import PinkPeony
from flower_market.singleton_meta import SingletonMeta


class PinkPeonyFactory(FlowerFactory, metaclass=SingletonMeta):

    def prepare(self, count: int = 1, artificial: bool = False, cutted: bool = False) -> PinkPeony:
        return PinkPeony(count, artificial, cutted)