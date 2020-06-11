from .pizza import Pizza


class Pepperoni(Pizza):
    def eat(self):
        print(f"eat {self.__class__.__name__}, attrs: {self.__dict__}")