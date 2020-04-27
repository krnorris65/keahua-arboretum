# from interfaces import IAquatic
from interfaces import Identifiable, IContainsAnimals, IContainsPlants
# from animals import RiverDolphin


class River(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.type = "River"
        self.animal_capacity = 12
        self.plant_capacity = 6
    


    def add_animal(self, animal):
        try:
            # check to see if the biome is at capacity, if it is raise an exception
            if not self.animals_at_capacity:
                if animal.aquatic and (animal.cell_type == "hypertonic" or animal.cell_type == "isotonic"):
                    self._IContainsAnimals__animals.append(animal)
            else:
                raise Exception
        except AttributeError:
            print("Cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        try:
            # check to see if the biome is at capacity, if it is raise an exception
            if not self.plants_at_capacity:
                if plant.aquatic and (plant.cell_type == "hypertonic" or plant.cell_type == "isotonic"):
                    self._IContainsPlants__plants.append(plant)
            else:
                raise Exception
        except AttributeError:
            print("Cannot add non-aquatic, or saltwater plants to a river")

