from factory.method.pasta.ita_bolognese import ItaBolognese
from factory.method.pasta.ita_carbonara import ItaCarbonara
from factory.method.pasta.ita_napoli import ItaNapoli
from factory.method.pasta.pasta import Pasta
from factory.method.pasta.restaurant import Restaurant


class ItaRestaurant(Restaurant):

    def _prepare_pasta(self, name: str, weight: int, parmesan: bool, al_dente=False) -> Pasta:
        if name == 'bolognese':
            return ItaBolognese(weight, parmesan, al_dente)
        elif name == 'carbonara':
            return ItaCarbonara(weight, parmesan, al_dente)
        elif name == 'napoli':
            return ItaNapoli(weight, parmesan, al_dente)
        else:
            return None
