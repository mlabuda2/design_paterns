from .pasta import Pasta


class ItaCarbonara(Pasta):
    def __init__(self, weight: int, parmesan: bool = False, al_dente=False):
        super().__init__(weight, parmesan, al_dente)
        self.typ = 'italy'

    def eat(self):
        print(f"eat {self.__class__.__name__}, attrs: {self.__dict__}")