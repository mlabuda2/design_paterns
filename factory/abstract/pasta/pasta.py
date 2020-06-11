from abc import ABC, abstractmethod


class Pasta(ABC):
    def __init__(self, weight: int, parmesan: bool = False, al_dente=False):
        self.weight = weight
        self.parmesan = parmesan
        self.al_dente = al_dente

    @abstractmethod
    def eat(self):
        pass

    def get_total_kcal(self):
        return self.weight * 5
