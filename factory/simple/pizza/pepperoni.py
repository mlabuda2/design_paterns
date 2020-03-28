from .pizza import Pizza


class Pepperoni(Pizza):
    def cook(self):
        print("cook ", self.__class__.__name__)
