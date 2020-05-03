from flower_market.flower.rose.rose import Rose
from flower_market.price_list.polish_price_builder import PolishPriceBuilder
from flower_market.price_list.german_price_builder import GermanPriceBuilder


class RedRose(Rose):
    @property
    def color(self):
        return 'Red'

    @property
    def margin(self) -> float:
        return 1.15


if __name__ == '__main__':
    r = RedRose(50)
    print(r.get_cost(PolishPriceBuilder))
    print(r.get_cost(GermanPriceBuilder))