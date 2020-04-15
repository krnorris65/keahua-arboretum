import os
from animals import RiverDolphin
from environments import River, Coastline
from .choose_annex import choose_annex

def release_animal(arboretum):
    '''
        Presents list of animals a user can choose to release into a biome in their arboretum. When the user selects an animal it creates an instance of that animal, determines which annexes can hold that animal and invokes the choose_annex function

        Arguments: 
            arboretum that animal will be released to
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    animal = None

    print("1. River Dolphin")
    print("2. Dragonfly")

    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = RiverDolphin()

        # river dolphin can go in either a river or coastline
        annex_options = arboretum.rivers + arboretum.coastlines
        choose_annex(arboretum, animal, annex_options)
    if choice == "2":
        pass



