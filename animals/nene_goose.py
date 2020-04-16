from animals import Animal
from interfaces import Identifiable, IWalking, IFlying

class NeneGoose(Animal, Identifiable, IWalking, IFlying):

    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        Identifiable.__init__(self)
        IWalking.__init__(self)
        IFlying.__init__(self)
        self.__prey = { "Plants" }
