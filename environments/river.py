# from interfaces import IAquatic
from interfaces import Identifiable, IContainsAnimals, IContainsPlants
# from animals import RiverDolphin


class River(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.__capacity = 12
    

    @property
    def animals(self):
        return self._IContainsAnimals__animals

    def add_animal(self, animal):
        try:
            if animal.aquatic and (animal.cell_type == "hypertonic" or animal.cell_type == "isotonic"):
                self._IContainsAnimals__animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-aquatic, or saltwater animals to a river")
    
    @property
    def animals_at_capacity(self):
        if len(self._IContainsAnimals__animals) == self.__capacity:
            return True
        else:
            return False

    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add plants that require brackish water or stagnant water to a river biome")
