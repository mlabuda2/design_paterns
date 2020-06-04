from flower_market.bouquet.custom_florist_factory import CustomFloristFactory
from flower_market.bouquet.funeral_florist_factory import FuneralFloristFactory
from flower_market.bouquet.valentines_florist_factory import ValentinesFloristFactory
from flower_market.client.client import Client
from flower_market.client.receipt import Receipt
from flower_market.client.shopping_cart import ShoppingCart
from flower_market.flower.lilac.white_lilac_factory import WhiteLilacFactory
from flower_market.flower.peony.pink_peony_factory import PinkPeonyFactory
from flower_market.flower.rose.red_rose_factory import RedRoseFactory
from flower_market.price_list.broker import Broker
from flower_market.price_list.price_list import Stock


def main():
    stock_a = Stock()  # observer
    broker = Broker()  # subject
    broker.attach(stock_a)

    valentines_florist = ValentinesFloristFactory()  # abstract factory

    matthew = Client('Matthew', 90.0, 'PL')
    matthew.get(valentines_florist.prepare_bouquet())
    matthew.pay()

    broker.its_time_to_fetch_prices()
    funeral_florist = FuneralFloristFactory()  # abstract factory + singleton
    maria = Client('Maria', 70.0, 'GR')
    maria.get(funeral_florist.prepare_bouquet())
    maria.pay()

    custom_florist = CustomFloristFactory()
    john = Client('John', 300.0, 'PL')
    john.get(RedRoseFactory().prepare(2))
    john.get(WhiteLilacFactory().prepare(3))
    john.get(PinkPeonyFactory().prepare(4))
    john.get(custom_florist.prepare_bouquet(john.takeout_shopping_cart()))

    j_shopping_cart: ShoppingCart = john.get_shopping_cart()
    print(j_shopping_cart)
    john.pay()
    print(john.get_cash())

    j_receipt: Receipt = john.get_purchase_history(1)[0]

    jessie = Client('Jessie', 300.0, 'GR')
    jessie.get_all(j_receipt.copy().products)  # prototype
    jessie.pay()

if __name__ == '__main__':
    main()
