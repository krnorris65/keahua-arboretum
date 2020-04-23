from animals import Animal
from interfaces import Identifiable, ISwimming, ISaltwater

class Ulae(Animal, Identifiable, ISwimming, ISaltwater):

    def __init__(self):
        Animal.__init__(self, "'Ulae", [ "Fish" ])
        Identifiable.__init__(self)
        ISwimming.__init__(self)
        ISaltwater.__init__(self)
