from .pasta import Pasta


class Napoli(Pasta):
    def cook(self):
        print("cook ", self.__class__.__name__)