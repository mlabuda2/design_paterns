a = 1
b = 1
print(id(a) == id(b))


class A:
    def __init__(self):
        self.a = 1


oa = A()
# print(oa.lock)
# Enter critical section
with self.lock:
    print(oa.a)
    # Do critical work

# Exit critical section


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
