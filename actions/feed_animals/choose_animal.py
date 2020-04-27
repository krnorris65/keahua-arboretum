import os

from helper.get_animals import get_animals
from .choose_food import choose_food

def choose_animal(selected_animal, arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    animals = get_animals(selected_animal, arboretum)

    print(f"Which {selected_animal} do you want to feed?")

    for index, animal in enumerate(animals):
        shortened_id = str(animal.id)[:8]
        print(f"{index + 1}. {animal.species} {shortened_id}")

    selection = input(">")
    try:
        feed_this_animal = animals[int(selection) - 1]
        choose_food(feed_this_animal)
    except IndexError:
        os.system('clear')
        input("Invalid selection. Press enter to choose again.")
        choose_animal(selected_animal, arboretum)
    except:
        pass
