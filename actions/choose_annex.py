import os
from helper.annex_options import get_annex_options


def choose_annex(arboretum, animal, display="initial", message=""):
    '''
        Presents list of biomes a user can choose to release a selected animal to.

        Arguments: 
            arboretum- that animal will be released to
            animal- the animal that will be released
            options- the options of biomes in the arboretum that animal can be released to
            display (optional)- what display message should appear when this function executes. default value is initial
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

    # determines what biomes can hold that animal
    list_of_options = get_annex_options(animal, arboretum)

    if display == "initial":
        print("**** Please select a biome ****")

    if display == "error":
        print(f"**** {message}, please choose another biome ****")

    if display == "invalid":
        print("**** Invalid Selection, please choose another biome ****")

    print("(Press enter to return to Main Screen)")
    print("")

    for index, option in enumerate(list_of_options):
        print(f'{index + 1}. {option.type} ({len(option.animals)} animals)')

    print("")
    print(f"Release the {animal.species} into which biome?")

    choice = input("> ")
    try:
        chosen_option = list_of_options[int(choice) - 1]

        # find the index of the chosen option in the correct list and add the animal to that list
        if(chosen_option.type == "River"):
            river_index = arboretum.rivers.index(chosen_option)
            river = arboretum.rivers[river_index]
            river.add_animal(animal)

        elif(chosen_option.type == "Coastline"):
            coastline_index = arboretum.coastlines.index(chosen_option)
            coastline = arboretum.coastlines[coastline_index]
            coastline.add_animal(animal)

        elif(chosen_option.type == "Forest"):
            forest_index = arboretum.forests.index(chosen_option)
            forest = arboretum.forests[forest_index]
            forest.add_animal(animal)

        elif(chosen_option.type == "Grassland"):
            grassland_index = arboretum.grasslands.index(chosen_option)
            grassland = arboretum.grasslands[grassland_index]
            grassland.add_animal(animal)

        elif(chosen_option.type == "Swamp"):
            swamp_index = arboretum.swamps.index(chosen_option)
            swamp = arboretum.swamps[swamp_index]
            swamp.add_animal(animal)

        elif(chosen_option.type == "Mountain"):
            mountain_index = arboretum.mountains.index(chosen_option)
            mountain = arboretum.mountains[mountain_index]
            mountain.add_animal(animal)

    except IndexError:
        # User entered invalid option, run choose_annex function with display="invalid"
        choose_annex(arboretum, animal, list_of_options, "invalid")
    except ValueError:
        # User entered value other than a number
        pass
    except AttributeError as error:
        choose_annex(arboretum, animal, list_of_options, "error", error)
    except Exception:
        # when an exception is raised from a conditional, run choose_annex function with display="error"
        choose_annex(arboretum, animal, list_of_options,
                     "error", "Biome already at capacity")
