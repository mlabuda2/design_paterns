from factory.abstract.pasta.bolognese_factory import BologneseFactory
from factory.abstract.pizza.pepperoni_factory import PepperoniFactory
from factory.abstract.seafood.clams_factory import ClamsFactory
from factory.abstract.pasta.bolognese_factory_reflection import BologneseFactoryReflection
from factory.abstract.pizza.pepperoni_factory_reflection import PepperoniFactoryReflection
from factory.abstract.seafood.clams_factory_reflection import ClamsFactoryReflection


def test_factory_with_reflection():
    bolognese_factory = BologneseFactoryReflection()
    bolognese = bolognese_factory.cook(111, True)
    bolognese.eat()

    clams_factory = ClamsFactoryReflection()
    clams = clams_factory.cook(10, None)
    clams.eat()

    pepperoni_factory = PepperoniFactoryReflection()
    pepperoni = pepperoni_factory.cook_double_dough(33, 'tomato')
    pepperoni.eat()


def test_factory():
    bolognese_factory = BologneseFactory()
    bolognese = bolognese_factory.cook(111, True)
    bolognese.eat()

    clams_factory = ClamsFactory()
    clams = clams_factory.cook(10, None)
    clams.eat()

    pepperoni_factory = PepperoniFactory()
    pepperoni = pepperoni_factory.cook_double_dough(33, 'tomato')
    pepperoni.eat()


if __name__ == '__main__':
    # test_factory()
    test = 'no_reflection'
    if test == 'reflection':
        for _ in range(100000):
            test_factory_with_reflection()
    else:
        for _ in range(100000):
            test_factory()