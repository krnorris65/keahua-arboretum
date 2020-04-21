from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class Mountain(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.animal_capacity = 15

    def add_animal(self, animal):
        try:
            # check to see if the biome is at capacity, if it is raise an exception that will be handled in choose_annex.py
            if not self.animals_at_capacity:
                if animal.terrestrial:
                    self._IContainsAnimals__animals.append(animal)
            else:
                raise Exception
        except AttributeError:
            raise AttributeError(
                "Cannot add non-terrestrial animals to a mountain")