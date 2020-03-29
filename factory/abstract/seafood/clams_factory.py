from threading import Lock

from factory.abstract.seafood.clams import Clams
from factory.abstract.seafood.seafood_abstract_factory import SeafoodFactory
from factory.abstract.singleton_meta import SingletonMeta
from factory.simple.seafood.seafood import Seafood


class ClamsFactory(SeafoodFactory):
    __instance = {}
    __lock = Lock()

    def __new__(cls):
        if type(object.__new__(cls)).__name__ not in cls.__instance:
            with cls.__lock:
                if type(object.__new__(cls)).__name__ not in cls.__instance:
                    cls.__instance[type(object.__new__(cls)).__name__] = object.__new__(cls)
        return cls.__instance[type(object.__new__(cls)).__name__]

    def cook(self, quantity: int, sauce: str) -> Seafood:
        return Clams(quantity, sauce)

    def serve_raw(self, quantity: int, sauce: str) -> Seafood:
        return Clams(quantity, sauce, raw=True)

