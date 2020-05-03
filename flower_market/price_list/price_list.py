from flower_market.price_list.cashbox import Cashbox


class Stock():

    def get_current_price(self, barcode: str) -> float:
        # TODO request to mocked stock api
        return 10.0


class PriceList:

    def get_product_barcode(self, name: str) -> str:
        # TODO request to db
        return '9388395052'

    def get_price(self, flower, Builder):
        base_price = Stock().get_current_price(self.get_product_barcode(flower.__class__.__name__))
        cashbox = Cashbox()
        builder = Builder(base_price, flower.margin)
        cashbox.calcuate(builder)
        return builder.price
