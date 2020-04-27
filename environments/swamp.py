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
        self.type = "Swamp"
        self.animal_capacity = 8
        self.plant_capacity = 12


    def add_animal(self, animal):
        try:
            # check to see if the biome is at capacity, if it is raise an exception
            if not self.animals_at_capacity:            
                if animal.can_be_in_stagnant_env == True:
                    self._IContainsAnimals__animals.append(animal)
            else:
                raise Exception                    
        except AttributeError:
            raise AttributeError(
                "This animal cannot survive in a stagnant environment")

    def add_plant(self, plant):
        try:
            # check to see if the biome is at capacity, if it is raise an exception
            if not self.plants_at_capacity:            
                if plant.can_be_in_stagnant_env == True:
                    self._IContainsPlants__plants.append(plant)
            else:
                raise Exception                    
        except AttributeError:
            raise AttributeError(
                "This plant cannot survive in a stagnant environment")

