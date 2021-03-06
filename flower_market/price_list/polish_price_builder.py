from flower_market.price_list.price_builder import PriceBuilder


class PolishPriceBuilder(PriceBuilder):

    @property
    def tax(self) -> float:
        return 1.23

    def add_export_cost(self):
        self.price._base = self.price._base * 1.00

    def set_net(self):
        self.price._net = self.price._base * self.price._margin

    def set_gross(self):
        self.price._gross = self.price._net * self.tax

    def set_tare(self):
        self.price._tare = self.price._gross - self.price._net
