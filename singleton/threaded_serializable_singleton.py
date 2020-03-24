from __future__ import annotations
from threading import Lock, Thread
from typing import Optional
import uuid
import weakref


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """
    _instance: Optional[Singleton] = None
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        # DCL
        # if not cls._instance:
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Singleton(metaclass=SingletonMeta):
    ident_cache = weakref.WeakValueDictionary()
    value: str = None

    def __new__(cls, identity=None, **kwargs):
        if identity is None:
            identity = uuid.uuid1()
        try:
            self = cls.ident_cache[identity]
        except KeyError:
            self = super(Singleton, cls).__new__(cls)
            self.__identity = identity
            self.__init__(**kwargs)
            cls.ident_cache[identity] = self
        return self

    def __getnewargs__(self):
        return (self.__identity,)

    def __init__(self, value: str) -> None:
        self.value = value


def get_singleton(value: str) -> None:
    singleton = Singleton(value=value)
    print(singleton.value)
    return singleton


def test_singleton():
    for _ in range(10000):
        process1 = Thread(target=get_singleton, args=("FOO",))
        process2 = Thread(target=get_singleton, args=("BAR",))
        process1.start()
        process2.start()
        # process1.join()
        # process2.join()


if __name__ == "__main__":
    # test_singleton()

    import pickle
    instance = get_singleton(1)
    instance2 = get_singleton(2)
    print(id(instance))
    print(id(instance2))

    instance3 = pickle.loads(pickle.dumps(instance, pickle.HIGHEST_PROTOCOL))
    instance4 = pickle.loads(pickle.dumps(instance))
    print(id(instance3))
    print(id(instance4))
    print(instance.value, instance2.value, instance3.value, instance4.value)
    print(instance._instance)
    print(instance2._instance)
    print(instance3._instance)