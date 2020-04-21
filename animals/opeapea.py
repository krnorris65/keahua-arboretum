from animals import Animal
from interfaces import Identifiable, IFlying

class Opeapea(Animal, Identifiable, IFlying):

    def __init__(self):
        Animal.__init__(self, "Ope'ape'a")
        Identifiable.__init__(self)
        IFlying.__init__(self)
        self.__prey = { "Insects", "Vegetation"}
