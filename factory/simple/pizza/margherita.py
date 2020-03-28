from .pizza import Pizza


class Margherita(Pizza):
    def cook(self):
        print("cook ", self.__class__.__name__)
