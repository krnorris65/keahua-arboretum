import os
from animals import RiverDolphin, GoldDustDayGecko, NeneGoose, Kikakapu, Pueo, Ulae, Opeapea, HappyFaceSpider
from .choose_biome import choose_biome

def release_animal(arboretum):
    '''
        Presents list of animals a user can choose to release into a biome in their arboretum. When the user selects an animal it creates an instance of that animal, determines which annexes can hold that animal and invokes the choose_annex function

        Arguments: 
            arboretum that animal will be released to
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    animal = None

    print("1. River Dolphin")
    print("2. Gold Dust Day Gecko")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    print("")
    print("Choose animal to release.")
    choice = input(" > ")

    if choice == "1":
        animal = RiverDolphin()

    if choice == "2":
        animal = GoldDustDayGecko()

    if choice == "3":
        animal = NeneGoose()

    if choice == "4":
        animal = Kikakapu()
    
    if choice == "5":
        animal = Pueo()
    
    if choice == "6":
        animal = Ulae()
    
    if choice == "7":
        animal = Opeapea()
    
    if choice == "8":
        animal = HappyFaceSpider()

    if not animal == None:
        choose_biome(arboretum, animal)
    else:
        input("Invalid selection. Press enter to return to main screen")





