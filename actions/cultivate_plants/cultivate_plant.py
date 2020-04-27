import os
def cultivate_plant(arboretum):
    '''
        Presents list of plants a user can choose to cultivate in a biome in their arboretum. When the user selects a plant it creates an instance of that plant, determines which biomes can hold that plant and invokes the choose_location function

        Arguments: 
            arboretum that plant will be cultivated in
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    plant = None

    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")

    print("")
    print("Choose plant to cultivate.")
    choice = input(" > ")