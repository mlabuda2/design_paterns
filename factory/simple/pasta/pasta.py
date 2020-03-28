from abc import ABC, abstractmethod


class Pasta(ABC):
    def __init__(self, weight, parmesan=False):
        self.weight = weight
        self.parmesan = parmesan

    @abstractmethod
    def cook(self):
        pass
