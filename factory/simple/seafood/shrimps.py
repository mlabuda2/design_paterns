from .seafood import Seafood


class Shrimps(Seafood):
    def eat(self):
        print(f"eat {self.__class__.__name__}, attrs: {self.__dict__}")