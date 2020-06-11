from factory.abstract.pasta.pasta import Pasta
from factory.abstract.pasta.pasta_abstract_factory import PastaFactory
from factory.abstract.singleton_meta import SingletonMeta
from factory.abstract.pasta.bolognese import Bolognese

class BologneseFactoryReflection(PastaFactory, metaclass=SingletonMeta):

    def cook(self, weight: int, parmesan: bool) -> Pasta:
        return self.get_instance('Bolognese', [weight, parmesan])

    def cook_al_dente(self, weight: int, parmesan: bool) -> Pasta:
        return self.get_instance('Bolognese', [weight, parmesan], {'al_dente': True})

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