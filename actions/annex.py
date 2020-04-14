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

    choice = input("Choose your habitat > ")

    if choice == "1":
        # river
        river = River()
        arboretum.rivers.append(river)
    if choice == "2":
        # swamp
        swamp = Swamp()
        arboretum.swamps.append(swamp)
    if choice == "3":
        # coastline
        coastline = Coastline()
        arboretum.coastlines.append(coastline)
    if choice == "4":
        # grassland
        grassland = Grassland()
        arboretum.grasslands.append(grassland)
    if choice == "5":
        # forest
        forest = Forest()
        arboretum.forests.append(forest)
    if choice == "6":
        # mountain
        mountain = Mountain()
        arboretum.mountains.append(mountain)
