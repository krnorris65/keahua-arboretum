def get_biome_options(inhabitant, arboretum):
    '''
        Determines what biomes an animal or plant can be released to based on if that animal meets certain conditions

        Arguments: 
            animal or plant that is being released
            arboretum that animal or plant will be released to
            
        Returns:
            list of biomes in the arboretum that the animal or plant can be released to
    '''
    biomes = []

    try: 
        # meets these conditions add rivers
        if inhabitant.aquatic and (inhabitant.cell_type == "hypertonic" or inhabitant.cell_type == "isotonic"):
            biomes.extend(arboretum.rivers)
    except:
        pass

    try:
        # meets these conditions add coastlines
        if inhabitant.aquatic and (inhabitant.cell_type == "hypotonic" or inhabitant.cell_type == "isotonic"):
            biomes.extend(arboretum.coastlines)
    except:
        pass
    
    try:
        # meets these conditions add forests
        if inhabitant.terrestrial and inhabitant.can_be_in_shade:
            biomes.extend(arboretum.forests)
    except:
        pass
    
    try:
        # meets these conditions add grasslands
        if inhabitant.terrestrial and inhabitant.can_handle_less_rain:
            biomes.extend(arboretum.grasslands)
    except:
        pass
    
    try:
        # meets these conditions add swamps
        if inhabitant.can_be_in_stagnant_env == True:
            biomes.extend(arboretum.swamps)
    except:
        pass
    
    try:
        # meets these conditions add mountains
        if inhabitant.terrestrial and inhabitant.can_handle_high_elevation:
            biomes.extend(arboretum.mountains)
    except:
        pass

    
    return biomes

