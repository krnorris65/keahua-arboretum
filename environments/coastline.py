from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class Coastline(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)

    @property
    def animals(self):
        return self._IContainsAnimals__animals

    def add_animal(self, animal):
        self._IContainsAnimals__animals.append(animal)
 