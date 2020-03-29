from threading import Lock

from factory.abstract.pasta.bolognese import Bolognese
from factory.abstract.pasta.pasta import Pasta
from factory.abstract.pasta.pasta_abstract_factory import PastaFactory


class BologneseFactory(PastaFactory):
    __instance = {}
    __lock = Lock()

    def __new__(cls):
        if type(object.__new__(cls)).__name__ not in cls.__instance:
            with cls.__lock:
                if type(object.__new__(cls)).__name__ not in cls.__instance:
                    cls.__instance[type(object.__new__(cls)).__name__] = object.__new__(cls)
        return cls.__instance[type(object.__new__(cls)).__name__]

    def cook(self, weight: int, parmesan: bool) -> Pasta:
        return Bolognese(weight, parmesan)

    def cook_al_dente(self, weight: int, parmesan: bool) -> Pasta:
        return Bolognese(weight, parmesan, al_dente=True)


