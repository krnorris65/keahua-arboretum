from plants import Plant
from interfaces import Identifiable

class MountainAppleTree(Plant, Identifiable):
    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree", "Partial", 17)
        Identifiable.__init__(self)