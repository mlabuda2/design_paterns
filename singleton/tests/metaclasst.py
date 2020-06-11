class Base(object):
    def __init__(self, val):
        print("BASE __init__(self, val):")
        self.val = val

    @classmethod
    def make_obj(cls, val):
        print("BASE make_obj(cls, val):")
        return cls(val+1)


class Derived(Base):
    def __init__(self, val):
        # In this super call, the second argument "self" is an object.
        # The result acts like an object of the Base class.
        super(Derived, self).__init__(val+2)

    @classmethod
    def make_obj(cls, val):
        # In this super call, the second argument "cls" is a type.
        # The result acts like the Base class itself.
        # return super(Derived, cls).make_obj(val)
        # ==
        return super().make_obj(val)

    @staticmethod
    def make_obj_s(val):
        # In this super call, the second argument "Derived" is a type.
        # The result acts like the Base class itself.
        return super(Derived, Derived).make_obj(val)


b1 = Base(0)
print(b1.val)
b2 = Base.make_obj(0)
print(b2.val)
d1 = Derived(0)
print(d1.val)
d2 = Derived.make_obj(0)
print(d2.val)
d3 = Derived.make_obj_s(0)
print(d3.val)
