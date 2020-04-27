from animals import Animal
from interfaces import Identifiable, IFlying, IHighElevation, IShade

class Opeapea(Animal, Identifiable, IFlying, IHighElevation, IShade):

    def __init__(self):
        Animal.__init__(self, "Ope'ape'a", [ "Insects", "Vegetation"])
        Identifiable.__init__(self)
        IFlying.__init__(self)
        IHighElevation.__init__(self)
        IShade.__init__(self)
