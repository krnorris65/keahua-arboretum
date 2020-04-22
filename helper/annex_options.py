def annex_options(animal):
    annexes = []

    # meets these conditions add river
    if animal.aquatic and (animal.cell_type == "hypertonic" or animal.cell_type == "isotonic"):
        pass

    # meets these conditions add coastline
    if animal.aquatic and (animal.cell_type == "hypotonic" or animal.cell_type == "isotonic"):
        pass
    
    # meets these conditions add forest
    if animal.terrestrial and animal.can_be_in_shade:
        pass
    
    # meets these conditions add grassland
    if animal.terrestrial and animal.can_handle_less_rain:
        pass
    
    # meets these conditions add swamp
    if animal.can_be_in_stagnant_env == True:
        pass
    
    # meets these conditions add mountain
    if animal.terrestrial and animal.can_handle_high_elevation:
        pass
