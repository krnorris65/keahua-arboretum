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
        choose_annex(arboretum, animal, annex_options)
    if choice == "2":
        pass



