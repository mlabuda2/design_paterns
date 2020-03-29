from factory.simple.pasta.pasta import Pasta
from factory.simple.pasta.bolognese import Bolognese
from factory.simple.pasta.napoli import Napoli
from factory.simple.pasta.carbonara import Carbonara
from factory.simple.pizza.pizza import Pizza
from factory.simple.pizza.hawaiian import Hawaiian
from factory.simple.pizza.margherita import Margherita
from factory.simple.pizza.pepperoni import Pepperoni
from factory.simple.seafood.seafood import Seafood
from factory.simple.seafood.clams import Clams
from factory.simple.seafood.fish_n_chips import FishNChips
from factory.simple.seafood.shrimps import Shrimps

from factory.simple.singleton_meta import SingletonMeta


class FactoryPasta(metaclass=SingletonMeta):

    def cook(self, name: str, weight: int, parmesan: bool) -> Pasta:
        if name == 'bolognese':
            return Bolognese(weight, parmesan)
        elif name == 'carbonara':
            return Carbonara(weight, parmesan)
        elif name == 'napoli':
            return Napoli(weight, parmesan)
        else:
            return None


class FactorySeafood(metaclass=SingletonMeta):

    def cook(self, name: str, quantity: int, sauce: str) -> Seafood:
        if name == 'clams':
            return Clams(quantity, sauce)
        elif name == 'fish_n_chips':
            return FishNChips(quantity, sauce)
        elif name == 'shripms':
            return Shrimps(quantity, sauce)
        else:
            return None


class FactoryPizza(metaclass=SingletonMeta):

    def cook(self, name: str, diameter: int, sauce: str) -> Pizza:
        if name == 'hawaiian':
            return Hawaiian(diameter, sauce)
        elif name == 'pepperoni':
            return Pepperoni(diameter, sauce)
        elif name == 'margherita':
            return Margherita(diameter, sauce)
        else:
            return None


if __name__ == '__main__':
    factory_pasta = FactoryPasta()
    factory_pasta.cook('napoli', 300, True).eat()

    factory_pizza = FactoryPizza()
    factory_pizza.cook('pepperoni', 30, 'ketchup').eat()

    factory_seafood = FactorySeafood()
    factory_seafood.cook('clams', 200, 'tomato').eat()