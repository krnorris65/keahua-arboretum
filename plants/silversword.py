from plants import Plant
from interfaces import Identifiable, ILittleRainfall

class Silversword(Plant, Identifiable, ILittleRainfall):
    def __init__(self):
        Plant.__init__(self, "Silversword", "Full", 22)
        Identifiable.__init__(self)
        ILittleRainfall.__init__(self)