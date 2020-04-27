from plants import Plant
from interfaces import Identifiable, ILittleRainfall, IStagnant, ITerrestrial
class BlueJadeVine(Plant, Identifiable, ILittleRainfall, IStagnant, ITerrestrial):
    def __init__(self):
        Plant.__init__(self, "Blue Jade Vine", "Partial", 0)
        Identifiable.__init__(self)
        ILittleRainfall.__init__(self)
        IStagnant.__init__(self)
        ITerrestrial.__init__(self)