from animals import Animal
from interfaces import Identifiable, IWalking, IShade

class GoldDustDayGecko(Animal, Identifiable, IWalking, IShade):

    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        Identifiable.__init__(self)
        IWalking.__init__(self, 4)
        IShade.__init__(self)
        self.__prey = { "Insects" }

    @property
    def prey(self):
        return self.__prey