from prototype.volume_prototype.volume import Volume


class VolumeManager:
    def __init__(self) -> None:
        self._volume_database = {}

    def get_by_idx(self, idx: int) -> Volume:
        return self._volume_database[idx]

    def add(self, idx: int, volume: Volume) -> None:
        self._volume_database.update({idx: volume})
