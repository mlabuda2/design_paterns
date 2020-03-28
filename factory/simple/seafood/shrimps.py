from .seafood import Seafood


class Shrimps(Seafood):
    def cook(self):
        print("cook ", self.__class__.__name__)
