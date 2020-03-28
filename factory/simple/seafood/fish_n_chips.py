from .seafood import Seafood


class FishNChips(Seafood):
    def cook(self):
        print("cook ", self.__class__.__name__)
