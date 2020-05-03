from adapter.TwoWayAdapter.iaircraft import IAirCraft


class AirCraft(IAirCraft):
    def take_off(self) -> None:
        print("Aircraft engine takeoff")
        self._height = 200
        self._airborne = True

