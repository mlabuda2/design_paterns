from factory.method.pasta.restaurant_ita import ItaRestaurant
from factory.method.pasta.restaurant_pl import PlRestaurant

if __name__ == '__main__':
    pl_restaurant = PlRestaurant()
    ita_restaurant = ItaRestaurant()

    napoli = pl_restaurant.order_pasta('napoli', 100, True, al_dente=True)
    napoli.eat()

    napoli = ita_restaurant.order_pasta('napoli', 20, False)
    napoli.eat()

    bolognese = pl_restaurant.order_pasta('bolognese', 444, True)
    bolognese.eat()

    bolognese = ita_restaurant.order_pasta('bolognese', 123, False)
    bolognese.eat()
