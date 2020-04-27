from helper.annex_animals import get_animals

def animal_menu(selected_animal, arboretum):
    animals = get_animals(selected_animal, arboretum)

    print(f"Which {selected_animal} do you want to feed?")

    for index, animal in enumerate(animals):
        shortened_id = str(animal.id)[0:8]
        print(f"{index + 1}. {animal.species} {shortened_id}")

    selection = input(">")
    try:
        feed_this_animal = animals[int(selection) - 1]
        return feed_this_animal
    except:
        animal_menu(selected_animal, arboretum)