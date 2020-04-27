def get_biome_options(animal, arboretum):
    '''
        Determines what biomes an animal can be released to based on if that animal meets certain conditions

        Arguments: 
            animal that is being released
            arboretum that animal will be released to
            
        Returns:
            list of biomes in the arboretum that the animal can be released to
    '''
    biomes = []

    try: 
        # meets these conditions add rivers
        if animal.aquatic and (animal.cell_type == "hypertonic" or animal.cell_type == "isotonic"):
            biomes.extend(arboretum.rivers)
    except:
        pass

    try:
        # meets these conditions add coastlines
        if animal.aquatic and (animal.cell_type == "hypotonic" or animal.cell_type == "isotonic"):
            biomes.extend(arboretum.coastlines)
    except:
        pass
    
    try:
        # meets these conditions add forests
        if animal.terrestrial and animal.can_be_in_shade:
            biomes.extend(arboretum.forests)
    except:
        pass
    
    try:
        # meets these conditions add grasslands
        if animal.terrestrial and animal.can_handle_less_rain:
            biomes.extend(arboretum.grasslands)
    except:
        pass
    
    try:
        # meets these conditions add swamps
        if animal.can_be_in_stagnant_env == True:
            biomes.extend(arboretum.swamps)
    except:
        pass
    
    try:
        # meets these conditions add mountains
        if animal.terrestrial and animal.can_handle_high_elevation:
            biomes.extend(arboretum.mountains)
    except:
        pass

    
    return biomes

