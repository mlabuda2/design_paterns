from abc import abstractmethod, ABC


class Price:
    def __init__(self) -> None:
        self._base = 0
        self._margin = 0
        self._net = 0
        self._gross = 0
        self._tare = 0

    @property
    def __repr__(self) -> float:
        return self._gross

    @property
    def gross(self) -> float:
        return self._gross

    @property
    def net(self) -> float:
        return self._net

    @property
    def tare(self) -> float:
        return self._tare
