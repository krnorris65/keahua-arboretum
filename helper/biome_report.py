def biome_report(environment):
    print(f'\n{environment.type} [{str(environment.id)[:8]}]')
    print(f'  Animals:')
    for animal in environment.animals:
        print(f'     {animal.species} [{str(animal.id)[:8]}]')
    print(f'  Plants:')
    for plant in environment.plants:
        print(f'     {plant.species} [{str(plant.id)[:8]}]')