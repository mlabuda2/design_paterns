from adapter.TwoWayAdapter.iseacraft import ISeaCraft


class SeaCraft(ISeaCraft):
    def increase_revs(self) -> None:
        self._speed += 10
        print("Seacraft engine increases revs to ", self._speed, " knots")
