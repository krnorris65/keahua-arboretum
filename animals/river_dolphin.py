from animals import Animal
from interfaces import IFreshSaltwater, Identifiable

class RiverDolphin(Animal, IFreshSaltwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "River Dolphin", [ "Trout", "Mackarel", "Salmon", "Sardine" ])
        IFreshSaltwater.__init__(self)
        Identifiable.__init__(self)

    # @property
    # def prey(self):
    #     return self.__prey

    # def feed(self, prey):
    #     if prey in self.__prey:
    #         print(f'The dolphin ate {prey} for a meal')
    #     else:
    #         print(f'The dolphin rejects the {prey}')


    def __str__(self):
        return f'Dolphin {self.id}. Eeee EeeEEeeeeEE!'
