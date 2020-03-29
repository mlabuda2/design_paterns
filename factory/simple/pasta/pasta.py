from abc import ABC, abstractmethod


class Pasta(ABC):
    def __init__(self, weight: int, parmesan: bool = False):
        self.weight = weight
        self.parmesan = parmesan

    @abstractmethod
    def eat(self):
        pass
