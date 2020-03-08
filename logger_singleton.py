# -*- coding: utf-8 -*-
import logging
import os
import datetime
import time


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print("call")
        print(cls._instances)
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# python 3 style
class MyLogger(object, metaclass=SingletonType):
    _logger = None

    # def __call__():
    #     print("call MyLogger")

    def __init__(self):
        print("init")
        self._logger = logging.getLogger("crumbs")
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')

        now = datetime.datetime.now()
        dirname = "./log"

        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        fileHandler = logging.FileHandler(dirname + "/log_" + now.strftime("%Y-%m-%d") + ".log")

        streamHandler = logging.StreamHandler()

        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

        self._logger.addHandler(fileHandler)
        self._logger.addHandler(streamHandler)

        print("Generate new instance")

    def get_logger(self):
        return self._logger


class A:
    pass


# a simple usecase
if __name__ == "__main__":
    # MyLogger()
    # logger = MyLogger.__call__().get_logger()
    logger = MyLogger().get_logger()
    # logger = MyLogger()
    # print(type(logger))
    # print(type(type(logger)))
    # print(type(type(type(logger))))
    # print(type(MyLogger))
    # print(type(type(MyLogger)))
    # print(type(A))
    # a = A()
    # print(type(a))
    logger.info("Hello, Logger")
    logger.debug("bug occurred")
    logger2 = MyLogger.__call__().get_logger()
    print(logger is logger2)
    # logger()
