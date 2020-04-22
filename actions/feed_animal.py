import os

def get_animals(annexes, species):
    list_of_animals = []
    for biome in annexes:
        if len(biome.animals) > 0:
            for animal in biome.animals:
                if animal.species == species:
                    list_of_animals.append(animal)
    return list_of_animals

def feed_animal(arboretum):
    '''Presents a list of animals a user can feed.

    Arguments: 
    arboretum that animal will be in
    '''
    # list all types of animals
    # once user selects an animal, create a list of all that animal in the arboretum (organize by biome)
    # from that list select a specfic animal to feed
    # once an animal is selected, display a menu of available food 
    # select type of food to feed animal and display message showing the animal was fed
    os.system('cls' if os.name == 'nt' else 'clear')

    print("1. River Dolphin")
    print("2. Gold Dust Day Gecko")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    print("")
    print("Choose type of animal to feed.")
    choice = input(" > ")

    if choice == "1":
        # river dolphin can only be in a river or coastline
        annex_list = arboretum.rivers + arboretum.coastlines

        animals_in_arboretum = get_animals(annex_list, "River Dolphin")

    if choice == "2":
        # geckos can only be in a the forest
        annex_list = arboretum.forests

        animals_in_arboretum = get_animals(annex_list, "Gold Dust Day Gecko")

    if choice == "3":
        # nene goose can only be in a grasslands
        annex_list = arboretum.grasslands

        animals_in_arboretum = get_animals(annex_list, "Nene Goose")

    
    if choice == "4":
        # kikakapu can only be in a swamps or rivers
        annex_list = arboretum.swamps + arboretum.rivers

        animals_in_arboretum = get_animals(annex_list, "Kīkākapu")
    
    if choice == "5":
        # pueo can only be in a grasslands or forests
        annex_list = arboretum.grasslands + arboretum.forests

        animals_in_arboretum = get_animals(annex_list, "Pueo")
    
    if choice == "6":
        # ulae can only be in a coastlines
        annex_list = arboretum.coastlines

        animals_in_arboretum = get_animals(annex_list, "'Ulae")
    
    if choice == "7":
        # ope'ape'a can only be in a forests or mountains
        annex_list = arboretum.forests + arboretum.mountains

        animals_in_arboretum = get_animals(annex_list, "Ope'ape'a")
    
    if choice == "8":
        # happy-face spider can only be in a swamp
        annex_list = arboretum.swamps

        animals_in_arboretum = get_animals(annex_list, "Hawaiian Happy-Face Spider")
