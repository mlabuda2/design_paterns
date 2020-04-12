from prototype.volume_prototype.volume import Volume
from prototype.volume_prototype.volume_manager import VolumeManager


def main():
    manager = VolumeManager()
    manager.add(1, Volume(1, 'ssd', {'owner': 'John'}))
    manager.add(2, Volume(2, 'hdd', {'owner': 'James'}))
    manager.add(3, Volume(3, 'hybrid', {'owner': 'Martin'}))

    # 1 == 4
    manager.add(4, manager.get_by_ident(1))
    # change 4 property
    manager.get_by_ident(4).volume_type = 'hdd'

    manager.get_by_ident(1).present()
    manager.get_by_ident(4).present()

    manager.add(5, manager.get_by_ident(1).copy())
    manager.get_by_ident(5).volume_type = 'ssd+hdd'

    manager.get_by_ident(1).present()
    manager.get_by_ident(5).present()


if __name__ == '__main__':
    main()
