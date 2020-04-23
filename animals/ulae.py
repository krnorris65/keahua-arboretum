from animals import Animal
from interfaces import Identifiable, ISwimming, ISaltwater

class Ulae(Animal, Identifiable, ISwimming, ISaltwater):

    def __init__(self):
        Animal.__init__(self, "'Ulae")
        Identifiable.__init__(self)
        ISwimming.__init__(self)
        ISaltwater.__init__(self)
        self.__prey = { "Fish"}

    @property
    def prey(self):
        return self.__prey