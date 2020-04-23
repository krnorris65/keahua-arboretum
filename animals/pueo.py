from animals import Animal
from interfaces import Identifiable, IFlying, IShade, ILittleRainfall

class Pueo(Animal, Identifiable, IFlying, IShade, ILittleRainfall):

    def __init__(self):
        Animal.__init__(self, "Pueo")
        Identifiable.__init__(self)
        IFlying.__init__(self)
        IShade.__init__(self)
        ILittleRainfall.__init__(self)
        self.__prey = { "Rodents" }

    @property
    def prey(self):
        return self.__prey