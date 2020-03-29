from factory.abstract.pasta.bolognese import Bolognese
from factory.abstract.pasta.pasta import Pasta
from factory.abstract.pasta.pasta_abstract_factory import PastaFactory


class BologneseFactory(PastaFactory):

    def cook(self, weight: int, parmesan: bool) -> Pasta:
        return Bolognese(weight, parmesan)

    def cook_al_dente(self, weight: int, parmesan: bool) -> Pasta:
        return Bolognese(weight, parmesan, al_dente=True)


