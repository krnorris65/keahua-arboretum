from animals import Animal
from interfaces import Identifiable, IFlying, IShade

class Pueo(Animal, Identifiable, IFlying, IShade):

    def __init__(self):
        Animal.__init__(self, "Pueo")
        Identifiable.__init__(self)
        IFlying.__init__(self)
        IShade.__init__(self)
        self.__prey = { "Rodents" }
