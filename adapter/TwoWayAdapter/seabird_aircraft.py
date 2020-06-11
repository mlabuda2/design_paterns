from adapter.TwoWayAdapter.aircraft import AirCraft
from adapter.TwoWayAdapter.iseacraft import ISeaCraft


class SeaBirdAir(AirCraft, ISeaCraft):
    def __init__(self) -> None:
        AirCraft.__init__(self)
        ISeaCraft.__init__(self)

    def take_off(self) -> None:
        super().take_off()
        if self._airborne:
            self._speed = 50

    def increase_revs(self) -> None:
        self._speed += 10
        print("Seacraft engine increases revs to ", self._speed, " knots")
        if self._speed > 40:
            self.take_off()
