from flower_market.bouquet.bouquet import Bouquet
from flower_market.bouquet.florist_factory import FloristFactory


class CustomFloristFactory(FloristFactory):
    def prepare_bouquet(self, flowers):
        return Bouquet(flowers)