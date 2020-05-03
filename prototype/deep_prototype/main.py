from prototype.deep_prototype.tag_list import TagList
from prototype.deep_prototype.volume import Volume
from prototype.deep_prototype.volume_manager import VolumeManager


def main():
    tags = TagList(['funny', 'great'])
    manager = VolumeManager()
    volume1 = Volume(1, 'ssd', {'owner': 'John', 'city': 'London', 'tags': tags})
    manager.add(1, volume1)
    # manager.add(2, Volume(2, 'hdd', {'owner': 'James', 'city': 'New York'}))
    # manager.add(3, Volume(3, 'hybrid', {'owner': 'Martin', 'city': 'Manchester'}))

    # 4 = 1
    manager.add(4, manager.get_by_idx(1))
    volume4 = manager.get_by_idx(4)
    volume4.volume_type = 'hdd'
    volume4.update_data('owner', 'James')
    tags.tags[0] = 'angry'

    manager.get_by_idx(1).present()
    manager.get_by_idx(4).present()
    print('\n')

    manager.add(5, manager.get_by_idx(1).deepcopy())
    manager.get_by_idx(5).volume_type = 'ssd20'
    manager.get_by_idx(5).update_data('city', 'Chicago')
    manager.get_by_idx(5).update_data('owner', 'Jessica')
    tags.tags[0] = 'bad'
    manager.get_by_idx(1).present()
    manager.get_by_idx(5).present()


if __name__ == '__main__':
    main()
