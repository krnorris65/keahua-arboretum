from plants import Plant
from interfaces import Identifiable, IShade

class RainbowEucalyptusTree(Plant, Identifiable, IShade):
    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", "Shade", 8)
        Identifiable.__init__(self)
        IShade.__init__(self)