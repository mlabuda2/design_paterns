from flower_market.flower.lilac.lilac import Lilac
from flower_market.price_list.polish_price_builder import PolishPriceBuilder
from flower_market.price_list.german_price_builder import GermanPriceBuilder


class WhiteLilac(Lilac):
    @property
    def color(self):
        return 'White'

    @property
    def margin(self) -> float:
        return 1.3


if __name__ == '__main__':
    r = WhiteLilac(50)
    print(r.get_cost(PolishPriceBuilder))
    print(r.get_cost(GermanPriceBuilder))