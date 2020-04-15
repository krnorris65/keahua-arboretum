import os
from environments import River, Coastline


def choose_annex(arboretum, animal, options, display="initial"):
    '''
        Presents list of biomes a user can choose to release a selected animal to.

        Arguments: 
            arboretum- that animal will be released to
            animal- the animal that will be released
            options- the options of biomes in the arboretum that animal can be released to
            display (optional)- what display message should appear when this function executes. default value is initial
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


    if display == "initial":
        print("**** Please select a biome ****")

    if display == "error":
        print("**** That biome is not large enough, please choose another one ****")

    if display == "invalid":
        print("**** Invalid Selection, please choose another one ****")
    
    print("(Press enter to return to Main Screen)")
    print("")

    
    for index, option in enumerate(options):
        if(type(option) == River):
            print(f'{index + 1}. River ({len(option.animals)} animals)')
        elif(type(option) == Coastline):
            print(f'{index + 1}. Coastline ({len(option.animals)} animals)')

    print("")
    print("Release the animal into which biome?")

    choice = input("> ")
    try:
        chosen_option = options[int(choice) - 1]

        # find the index of the chosen option in the correct list and add the animal to that list
        if(type(chosen_option) ==River):
            river_index = arboretum.rivers.index(chosen_option)
            river = arboretum.rivers[river_index]
            if not river.animals_at_capacity:
                river.add_animal(animal)
            else:
                # raise exception when animal can't be added to biome
                raise Exception  
        elif(type(chosen_option) == Coastline):
            coastline_index = arboretum.coastlines.index(chosen_option)
            arboretum.coastlines[coastline_index].add_animal(animal)
    except IndexError:
        # User entered invalid option, run choose_annex function with display="invalid"
        choose_annex(arboretum, animal, options, "invalid")
    except ValueError:
        # User entered value other than a number
        pass
    except Exception:
        # when an exception is raised from a conditional, run choose_annex function with display="error"
        choose_annex(arboretum, animal, options, "error")