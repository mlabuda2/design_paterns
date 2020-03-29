from factory.abstract.pasta.bolognese_factory import BologneseFactory
from factory.abstract.pizza.pepperoni_factory import PepperoniFactory
from factory.abstract.seafood.clams_factory import ClamsFactory

if __name__ == '__main__':
    bolognese_factory = BologneseFactory()
    bolognese = bolognese_factory.cook(111, True)
    bolognese.eat()

    clams_factory = ClamsFactory()
    clams = clams_factory.cook(10, None)
    clams.eat()

    pepperoni_factory = PepperoniFactory()
    pepperoni = pepperoni_factory.cook_double_dough(33, 'tomato')
    pepperoni.eat()
