# import sys
# sys.path.append('../')
# from animals.
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from interfaces import IStagnant


class Swamp(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)

    def animal_count(self):
        return "This place has a bunch of animals in it"

    def add_animal(self, animal):
        try:
            if animal.can_be_in_stagnant_env == True:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "This animal cannot survive in a stagnant environment")

