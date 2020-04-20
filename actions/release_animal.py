import os
from animals import RiverDolphin, GoldDustDayGecko, NeneGoose
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
    annex_options = []

    print("1. River Dolphin")
    print("2. Gold Dust Day Gecko")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = RiverDolphin()
        # river dolphin can go in either a river or coastline
        annex_options = arboretum.rivers + arboretum.coastlines

    if choice == "2":
        animal = GoldDustDayGecko()
        # geckos can only be released to the forest
        annex_options = arboretum.forests

    if choice == "3":
        animal = NeneGoose()
        # nene goose can only be released to grasslands
        annex_options = arboretum.grasslands

    
    if choice == "4":
        pass
        # animal = Kikakapu()
        # kikakapu can only be released to swamps or rivers
        # annex_options = arboretum.swamps + arboretum.rivers
    
    if choice == "5":
        pass
        # animal = Pueo()
        # pueo can only be released to grasslands or forests
        # annex_options = arboretum.grasslands + arboretum.forests
    
    if choice == "6":
        pass
        # animal = Ulae()
        # ulae can only be released to coastlines
        # annex_options = arboretum.coastlines
    
    if choice == "7":
        pass
        # animal = Opeapea()
        # ope'ape'a can only be released to forests or mountains
        # annex_options = arboretum.forests + arboretum.mountains
    
    if choice == "8":
        pass
        # animal = HappyFaceSpider()
        # happy-face spider can only be released to swamp
        # annex_options = arboretum.swamps

    
    choose_annex(arboretum, animal, annex_options)





