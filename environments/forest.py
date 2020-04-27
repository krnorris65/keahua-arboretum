from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class Forest(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.type = "Forest"
        self.animal_capacity = 20
        self.plant_capacity = 32


    def add_animal(self, animal):
        try:
            # check to see if the biome is at capacity, if it is raise an exception
            if not self.animals_at_capacity:
                if animal.terrestrial and animal.can_be_in_shade:
                    self._IContainsAnimals__animals.append(animal)
            else:
                raise Exception                    
        except AttributeError:
            raise AttributeError(
                "Cannot add non-terrestrial animals or animals that don't like shade to a forest")

    def add_plant(self, plant):
        try:
            # check to see if the biome is at capacity, if it is raise an exception
            if not self.plants_at_capacity:
                if plant.terrestrial and plant.can_be_in_shade:
                    self._IContainsPlants__plants.append(plant)
            else:
                raise Exception                    
        except AttributeError:
            raise AttributeError(
                "Cannot add non-terrestrial plants or plants that don't like shade to a forest")