class IContainsAnimals():

    def __init__(self):
        self.__animals = []
        self.animal_capacity = 0
    
    @property
    def animals(self):
        return self.__animals
        
    @property
    def animals_at_capacity(self):
        if len(self._IContainsAnimals__animals) == self.animal_capacity:
            return True
        else:
            return False

    # basic add animal method
    def add_animal(self, new_animal):
        if not self.animals_at_capacity:
            self.__animals.append(new_animal)