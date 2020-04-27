from plants import Plant
from interfaces import Identifiable, ILittleRainfall, ITerrestrial

class Silversword(Plant, Identifiable, ILittleRainfall, ITerrestrial):
    def __init__(self):
        Plant.__init__(self, "Silversword", "Full", 22)
        Identifiable.__init__(self)
        ILittleRainfall.__init__(self)
        ITerrestrial.__init__(self)