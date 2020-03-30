from factory.abstract.pizza.pepperoni import Pepperoni
from factory.abstract.pizza.pizza import Pizza
from factory.abstract.pizza.pizza_abstract_factory import PizzaFactory
from factory.abstract.singleton_meta import SingletonMeta


class PepperoniFactory(PizzaFactory, metaclass=SingletonMeta):

    def cook(self, diameter: int, sauce: bool) -> Pizza:
        return Pepperoni(diameter, sauce)

    def cook_double_dough(self, diameter: int, sauce: bool) -> Pizza:
        return Pepperoni(diameter, sauce, double_dough=True)


