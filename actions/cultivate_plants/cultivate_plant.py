import os
def cultivate_plant(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    plant = None

    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")

    print("")
    print("Choose plant to cultivate.")
    choice = input(" > ")