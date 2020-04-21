from animals import Animal
from interfaces import Identifiable, IWalking, IStagnant

class HappyFaceSpider(Animal, Identifiable, IWalking, IStagnant):

    def __init__(self):
        Animal.__init__(self, "Hawaiian Happy-Face Spider")
        Identifiable.__init__(self)
        IWalking.__init__(self, 8)
        IStagnant.__init__(self)
        self.__prey = { "Insects"}
