from plants import Plant
from interfaces import Identifiable, IShade, ITerrestrial

class RainbowEucalyptusTree(Plant, Identifiable, IShade, ITerrestrial):
    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", "Shade", 8)
        Identifiable.__init__(self)
        IShade.__init__(self)
        ITerrestrial.__init__(self)