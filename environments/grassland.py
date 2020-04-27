from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class Grassland(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.type = "Grassland"
        self.animal_capacity = 15
        self.plant_capacity = 15


    def add_animal(self, animal):
        try:
            # check to see if the biome is at capacity, if it is raise an exception that will be handled in choose_biome.py
            if not self.animals_at_capacity:
                if animal.terrestrial and animal.can_handle_less_rain:
                    self._IContainsAnimals__animals.append(animal)
            else:
                raise Exception
        except AttributeError:
            print("Cannot add add non-terrestrial animals or animals that need a lot of rain to a grassland")

    def add_plant(self, plant):
        try:
            # check to see if the biome is at capacity, if it is raise an exception
            if not self.plants_at_capacity:
                if plant.terrestrial and plant.can_handle_less_rain:
                    self._IContainsPlants__plants.append(plant)
            else:
                raise Exception
        except AttributeError:
            print("Cannot add add non-terrestrial plants or plants that need a lot of rain to a grassland")