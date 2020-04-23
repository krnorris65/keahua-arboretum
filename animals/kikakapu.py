from animals import Animal
from interfaces import Identifiable, ISwimming, IStagnant, IFreshwater

class Kikakapu(Animal, Identifiable, ISwimming, IStagnant, IFreshwater):

    def __init__(self):
        Animal.__init__(self, "Kīkākapu", ["Worms", "Sea Sponges", "Jellyfish", "Corals", "Molluscs"])
        Identifiable.__init__(self)
        ISwimming.__init__(self)
        IStagnant.__init__(self)
        IFreshwater.__init__(self)
