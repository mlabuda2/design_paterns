from flower_market.bouquet.bouquet import Bouquet
from flower_market.bouquet.florist_factory import FloristFactory
from flower_market.flower.rose.red_rose_factory import RedRoseFactory


class FuneralFloristFactory(FloristFactory):
    def prepare_bouquet(self):
        return Bouquet([RedRoseFactory().prepare(20)])