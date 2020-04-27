from plants import Plant
from interfaces import Identifiable

class RainbowEucalyptusTree(Plant, Identifiable):
    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", "Shade", 8)
        Identifiable.__init__(self)