from flower_market.flower.peony.peony import Peony
from flower_market.price_list.polish_price_builder import PolishPriceBuilder
from flower_market.price_list.german_price_builder import GermanPriceBuilder


class PinkPeony(Peony):
    @property
    def color(self) -> str:
        return 'Pink'

    @property
    def margin(self) -> float:
        return 1.5


if __name__ == '__main__':
    r = PinkPeony(50)
    print(r.get_cost(PolishPriceBuilder))
    print(r.get_cost(GermanPriceBuilder))