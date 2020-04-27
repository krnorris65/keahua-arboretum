from helper.biome_report import biome_report
def build_facility_report(arboretum):

    for river in arboretum.rivers:
        biome_report(river)

    for swamp in arboretum.swamps:
        biome_report(swamp)

    for coastline in arboretum.coastlines:
        biome_report(coastline)

    for grassland in arboretum.grasslands:
        biome_report(grassland)

    for forest in arboretum.forests:
        biome_report(forest)

    for mountain in arboretum.mountains:
        biome_report(mountain)

    input("\n\nPress any key to continue...")
