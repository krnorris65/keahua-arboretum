from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class Coastline(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.type = "Coastline"
        self.animal_capacity = 15
        self.plant_capacity = 3

    def add_animal(self, animal):
        try:
            # check to see if the biome is at capacity, if it is raise an exception
            if not self.animals_at_capacity:
                if animal.aquatic and (animal.cell_type == "hypotonic" or animal.cell_type == "isotonic"):
                    self._IContainsAnimals__animals.append(animal)
            else:
                raise Exception
        except AttributeError:
            raise AttributeError(
                "Cannot add non-aquatic, or freshwater animals to a coastline")

    def add_plant(self, plant):
        try:
            # check to see if the biome is at capacity, if it is raise an exception
            if not self.plants_at_capacity:
                if plant.aquatic and (plant.cell_type == "hypotonic" or plant.cell_type == "isotonic"):
                    self._IContainsPlants__plants.append(plant)
            else:
                raise Exception
        except AttributeError:
            raise AttributeError(
                "Cannot add non-aquatic, or freshwater plants to a coastline")
 