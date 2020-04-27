class IContainsPlants():

    def __init__(self):
        self.__plants = []
        self.plant_capacity = 0
    
    @property
    def plants(self):
        return self.__plants
        
    @property
    def plants_at_capacity(self):
        if len(self._IContainsPlants__plants) == self.plant_capacity:
            return True
        else:
            return False