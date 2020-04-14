import os
from environments import River, Coastline


def choose_annex(arboretum, animal, options, display):
    os.system('cls' if os.name == 'nt' else 'clear')

    if display == "error":
        print("You can't select this option")

    for index, option in enumerate(options):
        if(type(option) == River):
            print(f'{index + 1}. River ({len(option.animals)} animals)')
        elif(type(option) == Coastline):
            print(f'{index + 1}. Coastline ({len(option.animals)} animals)')
    
    print("Release the animal into which biome?")
    choice = input("> ")
    chosen_option = options[int(choice) - 1]

    # find the index of the chosen option in the correct list and add the animal to that list
    if(type(chosen_option) ==River):
        river_index = arboretum.rivers.index(chosen_option)
        river = arboretum.rivers[river_index]
        if not river.animals_at_capacity:
            river.add_animal(animal)
        else:
            print("this is not available")
            choose_annex(arboretum, animal, options, "error")
    elif(type(chosen_option) == Coastline):
        coastline_index = arboretum.coastlines.index(chosen_option)
        arboretum.coastlines[coastline_index].add_animal(animal)