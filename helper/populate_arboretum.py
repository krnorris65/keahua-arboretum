from environments import River, Swamp, Coastline, Grassland, Forest, Mountain
from animals import RiverDolphin, GoldDustDayGecko, NeneGoose, Kikakapu, Pueo, Ulae, Opeapea, HappyFaceSpider
from plants import BlueJadeVine, MountainAppleTree, RainbowEucalyptusTree, Silversword


def populate_arboretum(arboretum):
    '''
        Populates the arboretum with one of each environment and one of each appropriate animal within that environment

        Arguments: arboretum that user wants to populate
    '''
    river = River()
    dolphin_r = RiverDolphin()
    kikakapu_r = Kikakapu()
    river.add_animal(dolphin_r)
    river.add_animal(kikakapu_r)
    arboretum.annex_river(river)
    
    swamp = Swamp()
    kikakapu_s = Kikakapu()
    spider_s = HappyFaceSpider()
    swamp.add_animal(kikakapu_s)
    swamp.add_animal(spider_s)
    arboretum.annex_swamp(swamp)
    
    coastline = Coastline()
    ulae_c = Ulae()
    dolphin_c = RiverDolphin()
    coastline.add_animal(ulae_c)
    coastline.add_animal(dolphin_c)
    arboretum.annex_coastline(coastline)
    
    grassland = Grassland()
    pueo_g = Pueo()
    goose_g = NeneGoose()
    grassland.add_animal(pueo_g)
    grassland.add_animal(goose_g)
    arboretum.annex_grassland(grassland)
    
    forest = Forest()
    gecko_f = GoldDustDayGecko()
    pueo_f = Pueo()
    opeapea_f = Opeapea()
    forest.add_animal(gecko_f)
    forest.add_animal(pueo_f)
    forest.add_animal(opeapea_f)
    arboretum.annex_forest(forest)
    
    mountain = Mountain()
    opeapea_m = Opeapea()
    mountain.add_animal(opeapea_m)
    arboretum.annex_mountain(mountain)
