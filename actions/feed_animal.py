import os

from helper.annex_animals import get_animals
from helper.feed_menu_helpers import food_menu

from .choose_animal import animal_menu

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
    selected_animal = None

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
        selected_animal = "River Dolphin"

    if choice == "2":
        selected_animal = "Gold Dust Day Gecko"

    if choice == "3":
        selected_animal = "Nene Goose"

    if choice == "4":
        selected_animal = "Kīkākapu"
    
    if choice == "5":
        selected_animal = "Pueo"
    
    if choice == "6":
        selected_animal = "'Ulae"
    
    if choice == "7":
        selected_animal = "Ope'ape'a"
    
    if choice == "8":
        selected_animal = "Hawaiian Happy-Face Spider"


    if selected_animal != None:
        animal_menu(selected_animal, arboretum)


        # os.system('clear')
        # print(f"What would you like to feed the {selected_animal}?")
        # chosen_food = food_menu(animal_to_feed)

        # food_type = animal_to_feed.prey[int(chosen_food) - 1]

        # animal_to_feed.feed(food_type)
        # print()
        # input("Press enter to return to the main menu...")


