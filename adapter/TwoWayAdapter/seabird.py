from adapter.TwoWayAdapter.iaircraft import IAirCraft
from adapter.TwoWayAdapter.seacraft import SeaCraft


class SeaBird(SeaCraft, IAirCraft):
    def __init__(self) -> None:
        SeaCraft.__init__(self)
        IAirCraft.__init__(self)

    @property
    def airborne(self):
        return self._height > 50

    def take_off(self):
        while not self._airborne:
            self.increase_revs()

    def increase_revs(self):
        super().increase_revs()
        if self._speed > 40:
            self._height += 100
            self._airborne = True
