import os

def choose_food(animal):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"What would you like to feed the {animal.species}?")

    for index, food in enumerate(animal.prey):
        print(f"{index + 1}. {food}")

    chosen_food = input(">")

    try:
        food_type = animal.prey[int(chosen_food) - 1]

        animal.feed(food_type)
        input("\nPress enter to return to the main menu...")
    except IndexError:
        os.system('clear')
        input("Invalid selection. Press enter to choose again.")
        choose_food(animal)
    except:
        pass