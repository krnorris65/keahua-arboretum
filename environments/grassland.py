from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class Grassland(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.animal_capacity = 15


    def add_animal(self, animal):
        try:
            if animal.wing_count > 0:
                self._IContainsAnimals__animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-flying animals to a grassland")