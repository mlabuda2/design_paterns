from abc import abstractmethod, ABC


class ValentinesFloristFactory(ABC):
    @abstractmethod
    def prepare_bouquet(self): pass
