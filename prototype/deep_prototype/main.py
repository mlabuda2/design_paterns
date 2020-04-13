from prototype.deep_prototype.tag_list import TagList
from prototype.deep_prototype.volume import Volume
from prototype.deep_prototype.volume_manager import VolumeManager


def main():
    tags = TagList(['funny', 'great'])
    manager = VolumeManager()
    manager.add(1, Volume(1, 'ssd', {'owner': 'John', 'city': 'London', 'tags': tags}))
    # manager.add(2, Volume(2, 'hdd', {'owner': 'James', 'city': 'New York'}))
    # manager.add(3, Volume(3, 'hybrid', {'owner': 'Martin', 'city': 'Manchester'}))

    # 4 = 1
    manager.add(4, manager.get_by_ident(1))
    # change 4 property
    manager.get_by_ident(4).volume_type = 'hdd'
    manager.get_by_ident(4).update_data('owner', 'James')
    tags.tags[0] = 'angry'

    manager.get_by_ident(1).present()
    manager.get_by_ident(4).present()

    manager.add(5, manager.get_by_ident(1).deepcopy())
    manager.get_by_ident(5).update_data('city', 'Chicago')
    manager.get_by_ident(5).update_data('owner', 'Jessica')

    tags.tags[0] = 'bad'

    manager.get_by_ident(1).present()
    manager.get_by_ident(5).present()


if __name__ == '__main__':
    main()
