from abc import abstractmethod, ABC


class FloristFactory(ABC):
    @abstractmethod
    def prepare_bouquet(self): pass
