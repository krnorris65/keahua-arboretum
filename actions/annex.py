import os
from environments import River, Swamp, Coastline, Grassland, Forest, Mountain


def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Forest")
    print("6. Mountain")

    print("\nChoose what you want to annex.")
    choice = input(" >")

    if choice == "1":
        # river
        river = River()
        arboretum.annex_river(river)
    if choice == "2":
        # swamp
        swamp = Swamp()
        arboretum.annex_swamp(swamp)
    if choice == "3":
        # coastline
        coastline = Coastline()
        arboretum.annex_coastline(coastline)
    if choice == "4":
        # grassland
        grassland = Grassland()
        arboretum.annex_grassland(grassland)
    if choice == "5":
        # forest
        forest = Forest()
        arboretum.annex_forest(forest)
    if choice == "6":
        # mountain
        mountain = Mountain()
        arboretum.annex_mountain(mountain)
