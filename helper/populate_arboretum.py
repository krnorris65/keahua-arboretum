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
    blue_jade_s = BlueJadeVine()
    swamp.add_animal(kikakapu_s)
    swamp.add_animal(spider_s)
    swamp.add_plant(blue_jade_s)
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
    blue_jade_g = BlueJadeVine()
    silversword_g = Silversword()
    grassland.add_animal(pueo_g)
    grassland.add_animal(goose_g)
    grassland.add_plant(blue_jade_g)
    grassland.add_plant(silversword_g)
    arboretum.annex_grassland(grassland)
    
    forest = Forest()
    gecko_f = GoldDustDayGecko()
    pueo_f = Pueo()
    opeapea_f = Opeapea()
    rainbow_tree_f = RainbowEucalyptusTree()
    forest.add_animal(gecko_f)
    forest.add_animal(pueo_f)
    forest.add_animal(opeapea_f)
    forest.add_plant(rainbow_tree_f)
    arboretum.annex_forest(forest)
    
    mountain = Mountain()
    opeapea_m = Opeapea()
    mountain_tree_m = MountainAppleTree()
    mountain.add_animal(opeapea_m)
    mountain.add_plant(mountain_tree_m)
    arboretum.annex_mountain(mountain)
