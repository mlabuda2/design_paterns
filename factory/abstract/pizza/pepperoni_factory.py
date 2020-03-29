from threading import Lock

from factory.abstract.pasta.bolognese import Bolognese
from factory.abstract.pizza.pepperoni import Pepperoni
from factory.abstract.pizza.pizza import Pizza
from factory.abstract.pizza.pizza_abstract_factory import PizzaFactory


class PepperoniFactory(PizzaFactory):
    __instance = {}
    __lock = Lock()

    def __new__(cls):
        if type(object.__new__(cls)).__name__ not in cls.__instance:
            with cls.__lock:
                if type(object.__new__(cls)).__name__ not in cls.__instance:
                    cls.__instance[type(object.__new__(cls)).__name__] = object.__new__(cls)
        return cls.__instance[type(object.__new__(cls)).__name__]

    def cook(self, diameter: int, sauce: bool) -> Pizza:
        return Pepperoni(diameter, sauce)

    def cook_double_dough(self, diameter: int, sauce: bool) -> Pizza:
        return Pepperoni(diameter, sauce, double_dough=True)


