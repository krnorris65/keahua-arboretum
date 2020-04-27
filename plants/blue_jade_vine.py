from plants import Plant
from interfaces import Identifiable, ILittleRainfall, IStagnant
class BlueJadeVine(Plant, Identifiable, ILittleRainfall, IStagnant):
    def __init__(self):
        Plant.__init__(self, "Blue Jade Vine", "Partial", 0)
        Identifiable.__init__(self)
        ILittleRainfall.__init__(self)
        IStagnant.__init__(self)