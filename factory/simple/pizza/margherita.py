from .pizza import Pizza


class Margherita(Pizza):
    def eat(self):
        print(f"eat {self.__class__.__name__}, attrs: {self.__dict__}")