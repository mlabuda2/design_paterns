import time

from flower_market.price_list.broker import Broker
from flower_market.price_list.cashbox import Cashbox
from flower_market.price_list.observer_pattern.observer import Observer
from flower_market.singleton_meta import SingletonMeta


class PriceFetchingException(Exception):
    pass


class Stock(Observer, metaclass=SingletonMeta):
    def __init__(self):
        print("Stock initiation")
        self.prices = {}
        self.__fetch_prices(coefficient=1.0)
        self.lock = False

    def get_current_price(self, barcode: str) -> float:
        # TODO
        if self.lock:
            raise PriceFetchingException()
        return 10.0

    def __fetch_prices(self, coefficient):
        self.prices = {}
        print("Stock prices updated")
        return True

    # Observer - Receiving update from subject.
    def update(self, broker: Broker):
        self.lock = True
        fetched = False
        while not fetched:
            fetched = self.__fetch_prices(broker.coefficient)
        self.lock = False


class PriceList:

    def get_product_barcode(self, name: str) -> str:
        # TODO request to db
        return '9388395052'

    def get_price(self, flower, Builder):
        base_price = None
        while not base_price:
            try:
                base_price = Stock().get_current_price(self.get_product_barcode(flower.__class__.__name__))
            except PriceFetchingException:
                time.sleep(3)
                continue
        cashbox = Cashbox()
        builder = Builder(base_price, flower.margin)
        cashbox.calcuate(builder)
        return builder.price
