from flower_market.bouquet.bouquet import Bouquet
from flower_market.bouquet.florist_factory import FloristFactory
from flower_market.flower.lilac.white_lilac_factory import WhiteLilacFactory
from flower_market.flower.peony.pink_peony_factory import PinkPeonyFactory
from flower_market.flower.rose.red_rose_factory import RedRoseFactory


class ValentinesFloristFactory(FloristFactory):
    def prepare_bouquet(self) -> Bouquet:
        return Bouquet([RedRoseFactory().prepare(2),
                        WhiteLilacFactory().prepare(2),
                        PinkPeonyFactory().prepare(2)])