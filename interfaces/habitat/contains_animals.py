class IContainsAnimals():

    def __init__(self):
        self.__animals = []
        self.animal_capacity = 0
    
    @property
    def animals_at_capacity(self):
        if len(self._IContainsAnimals__animals) == self.animal_capacity:
            return True
        else:
            return False
