from abc import abstractmethod, ABC

from factory.method.pasta.pasta import Pasta
from factory.method.singleton_meta import SingletonMeta


class Restaurant(ABC, metaclass=SingletonMeta):

    @abstractmethod
    def _prepare_pasta(self, name: str, weight: int, parmesan: bool, al_dente=False) -> Pasta:
        pass

    def order_pasta(self, name: str, weight: int, parmesan: bool, al_dente=False) -> Pasta:
        pasta = self._prepare_pasta(name, weight, parmesan, al_dente)
        return pasta
