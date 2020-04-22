from animals import Animal
from interfaces import Identifiable, IWalking, IFlying, ILittleRainfall

class NeneGoose(Animal, Identifiable, IWalking, IFlying, ILittleRainfall):

    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        Identifiable.__init__(self)
        IWalking.__init__(self)
        IFlying.__init__(self)
        ILittleRainfall.__init__(self)
        self.__prey = { "Plants" }
