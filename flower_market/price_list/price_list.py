import time

from flower_market.price_list.broker import Broker
from flower_market.price_list.cashbox import Cashbox
from flower_market.price_list.observer_pattern.observer import Observer
from flower_market.price_list.price import Price
from flower_market.singleton_meta import SingletonMeta


class PriceFetchingException(Exception):
    pass


class Stock(Observer, metaclass=SingletonMeta):
    BASE_PRICES = {
        'Rose': 10,
        'Peony': 8,
        'Lilac': 15
    }

    _stock_lock = False

    def __init__(self) -> None:
        print("Stock initiation")
        self.prices = {}
        self.__fetch_prices(coefficient=1.0)

    def get_current_price(self, product_name: str) -> float:
        if self._stock_lock:
            raise PriceFetchingException()
        return self.prices.get(product_name)

    def __fetch_prices(self, coefficient: float) -> bool:
        for product, price in self.BASE_PRICES.items():
            self.prices.update({product: price * coefficient})
        print("Stock prices updated")
        return True

    # Observer - Receiving update from subject.
    def update(self, broker: Broker) -> None:
        self._stock_lock = True
        print(f"Locked Stock!")
        time.sleep(10)
        fetched = False
        while not fetched:
            fetched = self.__fetch_prices(broker.coefficient)
        self._stock_lock = False
        print(f"Unlocked Stock!")


class PriceList:

    def get_price(self, flower: object, Builder) -> Price:
        base_price = None
        while not base_price:
            try:
                base_price = Stock().get_current_price(product_name=flower.name)
            except PriceFetchingException:
                print("Waiting for price fetching!")
                time.sleep(2)
                continue
        cashbox = Cashbox()
        builder = Builder(base_price, flower.margin)
        cashbox.calcuate(builder)
        return builder.price
