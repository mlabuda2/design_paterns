from abc import ABC


class VPC(ABC):
    def __init__(self):
        self._properties = {}

    def get_vpc(self):
        for key, value in self._properties.items():
            print(f"{key}: {value}")

    def set_property(self, key, value):
        self._properties.update({key: value})