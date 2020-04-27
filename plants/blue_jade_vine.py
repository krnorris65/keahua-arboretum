from plants import Plant
from interfaces import Identifiable
class BlueJadeVine(Plant, Identifiable):
    def __init__(self):
        Plant.__init__(self, "Blue Jade Vine", "Partial", 0)
        Identifiable.__init__(self)