from .pasta import Pasta


class Carbonara(Pasta):
    def cook(self):
        print("cook ", self.__class__.__name__)