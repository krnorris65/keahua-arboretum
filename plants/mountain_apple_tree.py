from plants import Plant
from interfaces import Identifiable, IHighElevation, ITerrestrial

class MountainAppleTree(Plant, Identifiable, IHighElevation, ITerrestrial):
    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree", "Partial", 17)
        Identifiable.__init__(self)
        IHighElevation.__init__(self)
        ITerrestrial.__init__(self)