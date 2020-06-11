from factory.method.pasta.pasta import Pasta
from factory.method.pasta.pl_bolognese import PlBolognese
from factory.method.pasta.pl_carbonara import PlCarbonara
from factory.method.pasta.pl_napoli import PlNapoli
from factory.method.pasta.restaurant import Restaurant
from factory.method.singleton_meta import SingletonMeta


class PlRestaurant(Restaurant, metaclass=SingletonMeta):

    def _prepare_pasta(self, name: str, weight: int, parmesan: bool, al_dente=False) -> Pasta:
        if name == 'bolognese':
            return PlBolognese(weight, parmesan, al_dente)
        elif name == 'carbonara':
            return PlCarbonara(weight, parmesan, al_dente)
        elif name == 'napoli':
            return PlNapoli(weight, parmesan, al_dente)
        else:
            return None
