from .pasta import Pasta


class Bolognese(Pasta):
    def cook(self):
        print("cook ", self.__class__.__name__)