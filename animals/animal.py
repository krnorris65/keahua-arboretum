class Animal:

    def __init__(self, species, prey=[]):
        self.species = species
        self.age = 0
        self.__prey = prey

    def move(self, propulsion, speed):
        return f"{self. species} moves at {speed} meters/sec by {propulsion}"

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The {self.species} ate {prey} for a meal')
        else:
            print(f'The {self.species} rejects the {prey}')
