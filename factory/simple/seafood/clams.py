from .seafood import Seafood


class Clams(Seafood):
    def cook(self):
        print("cook ", self.__class__.__name__)
