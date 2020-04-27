def get_animals(species, arboretum):
    '''Presents a list of animals a user can feed.

    Arguments: 
    species of the animal that was selected
    arboretum that animal will be in
    '''
    list_of_animals = []

    for biome in arboretum.all_biomes:
        # check to see if there are any animals in that biome
        if len(biome.animals) > 0:
            # if so, only add the animals that match the species to the list_of_animals
            for animal in biome.animals:
                if animal.species == species:
                    list_of_animals.append(animal)

    return list_of_animals