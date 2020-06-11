from prototype.volume_prototype.volume import Volume
from prototype.volume_prototype.volume_manager import VolumeManager


def main():
    manager = VolumeManager()
    volume1 = Volume(1, 'ssd', {'owner': 'John'})
    volume2 = Volume(2, 'hdd', {'owner': 'James'})
    volume3 = Volume(3, 'hybrid', {'owner': 'Martin'})
    manager.add(1, volume1)
    manager.add(2, volume2)
    manager.add(3, volume3)

    manager.add(4, manager.get_by_idx(1))

    volume4 = manager.get_by_idx(4)
    volume4.volume_type = 'hdd'

    manager.get_by_idx(1).present()
    manager.get_by_idx(4).present()

    manager.add(5, manager.get_by_idx(1).copy())
    volume5 = manager.get_by_idx(5)

    volume5.volume_type = 'ssd+hdd'
    volume5.update_data('owner', 'Test2')

    manager.get_by_idx(1).present()
    manager.get_by_idx(5).present()


if __name__ == '__main__':
    main()
