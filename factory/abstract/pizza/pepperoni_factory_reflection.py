from factory.abstract.pizza.pizza import Pizza
from factory.abstract.pizza.pizza_abstract_factory import PizzaFactory
from factory.abstract.singleton_meta import SingletonMeta
from factory.abstract.pizza.pepperoni import Pepperoni


class PepperoniFactoryReflection(PizzaFactory, metaclass=SingletonMeta):

    def cook(self, diameter: int, sauce: bool) -> Pizza:
        return self.get_instance('Pepperoni', [diameter, sauce])

    def cook_double_dough(self, diameter: int, sauce: bool) -> Pizza:
        return self.get_instance('Pepperoni', [diameter, sauce], {'double_dough': True})

    """ Class registration using reflection """
    def get_instance(self, classname: str, args: set = [], kwargs: dict = {}):
        if classname not in globals():
            raise Exception(f"Classname: {classname} not exist.")
        class_obj = globals()[classname]
        instance = class_obj(*args, **kwargs)
        return instance


    # """ Class creation and registration using reflection """
    # def get_instance(self, classname: str, baseclass: object, args: set = [], kwargs: dict = {}):
    #     baseclass_methods = self.get_methods2(baseclass)
    #     print(baseclass_methods)
    #     class_obj = type(classname, (baseclass,), baseclass_methods)
    #     if classname not in globals():
    #         print('classname not exist')
    #         globals()[classname] = class_obj
    #     print(class_obj)
    #     print(args)
    #     print(kwargs)
    #     instance = class_obj(*args, **kwargs)
    #     print("inst", dir(instance))
    #     return instance

    # """ Get abstract methods using refection """
    # def get_methods(self, baseclass: object):
    #     methods = [method_name for method_name in dir(baseclass) if method_name.find('_')]
    #     methods_dict = {}
    #     for m in methods:
    #         methods_dict.update({m: lambda self: ()})
    #     return methods_dict