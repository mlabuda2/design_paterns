from factory.abstract.seafood.clams import Clams
from factory.abstract.seafood.seafood_abstract_factory import SeafoodFactory
from factory.abstract.singleton_meta import SingletonMeta
from factory.simple.seafood.seafood import Seafood


class ClamsFactory(SeafoodFactory, metaclass=SingletonMeta):

    def cook(self, quantity: int, sauce: str) -> Seafood:
        return Clams(quantity, sauce)

    def serve_raw(self, quantity: int, sauce: str) -> Seafood:
        return Clams(quantity, sauce, raw=True)

