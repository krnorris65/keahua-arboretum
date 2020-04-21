from animals import Animal
from interfaces import Identifiable, IFlying

class Pueo(Animal, Identifiable, IFlying):

    def __init__(self):
        Animal.__init__(self, "Pueo")
        Identifiable.__init__(self)
        IFlying.__init__(self)
        self.__prey = { "Rodents" }
