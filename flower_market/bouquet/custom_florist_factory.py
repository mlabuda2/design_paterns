from flower_market.bouquet.bouquet import Bouquet


class CustomFloristFactory:
    def prepare_bouquet(self, flowers):
        return Bouquet(flowers)