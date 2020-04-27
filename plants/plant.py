class Plant:

    def __init__(self, species, sunlight, seeds=0):
        self.__species = species
        self.__peak_season = ""
        self.__sunlight = sunlight
        self.__seeds_produced = seeds
    
    @property
    def species(self):
        return self.__species

    @property
    def sunlight(self):
        return self.__sunlight

    @property
    def seeds_produced(self):
        return self.__seeds_produced
