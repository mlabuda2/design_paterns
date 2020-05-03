from flower_market.price_list.price_builder import PriceBuilder
from flower_market.singleton_meta import SingletonMeta


class Cashbox(metaclass=SingletonMeta):
    def calcuate(self, price_builder: PriceBuilder) -> None:
        price_builder.add_export_cost()
        price_builder.set_net()
        price_builder.set_gross()
        price_builder.set_tare()
