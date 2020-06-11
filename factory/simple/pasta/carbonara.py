from .pasta import Pasta


class Carbonara(Pasta):
    def eat(self):
        print(f"eat {self.__class__.__name__}, attrs: {self.__dict__}")