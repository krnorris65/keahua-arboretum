import os
from animals import RiverDolphin
from environments import River, Coastline
from .choose_annex import choose_annex

def release_animal(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    animal = None

    print("1. River Dolphin")
    print("2. Dragonfly")

    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = RiverDolphin()

        # river dolphin can go in either a river or coastline
        annex_options = arboretum.rivers + arboretum.coastlines
        choose_annex(arboretum, animal, annex_options, "initial")
    if choice == "2":
        pass

    # iterate through all options for that animal
    # for index, option in enumerate(annex_options):
    #     if(type(option) == River):
    #         print(f'{index + 1}. River ({len(option.animals)} animals)')
    #     elif(type(option) == Coastline):
    #         print(f'{index + 1}. Coastline ({len(option.animals)} animals)')
    
    # print("Release the animal into which biome?")
    # choice = input("> ")
    # chosen_option = annex_options[int(choice) - 1]

    # find the index of the chosen option in the correct list and add the animal to that list
    # if(type(chosen_option) ==River):
    #     river_index = arboretum.rivers.index(chosen_option)
    #     river = arboretum.rivers[river_index]
    #     if not river.animals_at_capacity:
    #         river.add_animal(animal)
    #     else:
    #         return
    #         # chosen_option = choose_annex(annex_options, "error")
    # elif(type(chosen_option) == Coastline):
    #     coastline_index = arboretum.coastlines.index(chosen_option)
    #     arboretum.coastlines[coastline_index].add_animal(animal)







    # arboretum.rivers[int(choice) - 1].animals.append(animal)


