# class MyMeta(type):
#     _instances = {}

#     def __call__(cls, *args, **kwargs):
#         if cls not in MyMeta._instances:
#             MyMeta._instances[cls] = super().__call__(*args, **kwargs)
#         return MyMeta._instances[cls]


# class Singleton(metaclass=MyMeta):
#     pass


class Singleton(object):
    def __new__(cls):
        print(dir(cls))
        print(cls.instance)
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


x = Singleton()
y = Singleton()
print(x is y)  # Outputs True
# while x is y:
#     x = Singleton()
#     y = Singleton()
#     print(x is y)  # Outputs True
