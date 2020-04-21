import os

def feed_animal(arboretum):
    '''Presents a list of animals a user can feed.

    Arguments: 
    arboretum that animal will be released to
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