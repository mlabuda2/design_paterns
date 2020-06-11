from __future__ import annotations
import copy
from abc import ABC, abstractmethod


class VolumePrototype(ABC):
    @abstractmethod
    def deepcopy(self): pass


class Volume(VolumePrototype):
    def __init__(self, ident: int, volume_type: str, data: dict) -> None:
        self._ident = ident
        self._volume_type = volume_type
        self._data = data

    @property
    def volume_type(self):
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        self._volume_type = volume_type

    @property
    def data(self):
        return self.data

    def update_data(self, key, value):
        self._data[key] = value

    def deepcopy(self) -> Volume:
        return copy.deepcopy(self)

    def present(self) -> None:
        print(f"Volume {self.__class__.__name__}, attrs: {self.__dict__} id {id(self)}")
