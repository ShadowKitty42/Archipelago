from ast import Tuple
import typing
from BaseClasses import Item, ItemClassification

class CotLItem(Item):  # or from Items import MyGameItem
    game = "Cult of the Lamb"  # name of the game/world this item is from

class ItemData:
    itemName: str
    progression: ItemClassification
    upgrade_name: str
    def __init__(self, itemName, progression, upgrade_name):
        self.itemName = itemName
        self.progression = progression
        self.upgrade_name = upgrade_name


mygame_items: typing.List[ItemData] = [

 # Shrine Items 

    #Tier 1 
    #ItemData("Temple", ItemClassification.useful), #Type: Building_Temple
    ItemData("Progressive Bed", ItemClassification.useful, "Prog_Bed"), #Type: Building_Beds
    #will need make this a progressive bed due to how its built sleeping bag
    ItemData("Body Pit", ItemClassification.useful, "Building_BodyPit"), #Type: Building_BodyPit
    #may need logic due to possibility of killing all base from infection
    ItemData("Farm Plot", ItemClassification.useful, "Building_Farms"), #Type: Building_Farms
    #may need to be logic to keep cultists alive to open areas
    ItemData("Progressive Farming Station", ItemClassification.useful, "Prog_FarmStation"), #Type: Building_FollowerFarming
    #may need to be logic to keep cultists alive to open areas
    ItemData("Seed Silo", ItemClassification.useful, "Building_FollowerFarming"), #Type: Building_SiloSeed
    ItemData("Tailor", ItemClassification.filler, "Building_Tailor"), #Type: Building_Tailor
    
    #Tier 2
    ItemData("Progressive Shrine & Temple Upgrade", ItemClassification.useful, "Prog_Temple"), #Type: Building_Temple2
    #Progressive
    ItemData("Basic Decorations", ItemClassification.filler, "Building_Decorations1"), 
    ItemData("Progressive Bed", ItemClassification.useful, "Prog_Bed"), #Type: Building_BetterBeds
    #Progressive bed 2 shelter
    ItemData("Offering Statue", ItemClassification.useful, "Shrine_OfferingStatue"), #Type: Shrine_OfferingStatue
    ItemData("Progressive Tabernacle", ItemClassification.useful, "Prog_Tabernacle"), #Type: Shrine_PassiveShrines
    ItemData("Prison", ItemClassification.useful, "Building_Prison"), #Type: Building_Prison
    ItemData("Progressive Lumberyard", ItemClassification.progression, "Prog_Lumberjack"), #Type: Economy_Lumberyard
    ItemData("Progressive Stone Mine", ItemClassification.progression, "Prog_Mine"), #Type: Economy_Mine
    #need to check note as I believe bloodstone mine is not what it said before I started the Woolhaven DLC
    ItemData("Progressive Missionary", ItemClassification.useful, "Prog_Missionary"), #Type: Building_Missionary
    ItemData("Progressive Demonic Summoning Circle", ItemClassification.useful, "Prog_DemonSummoner"), #Type: Building_DemonSummoner
    #should also be a progressive item
    ItemData("Progressive Scarecrow", ItemClassification.useful, "Prog_Scarecrow"), #Type: Building_AdvancedFarming
    
    #Tier 3
    ItemData("Progressive Refinery", ItemClassification.progression, "Prog_Refinery"), #Type: Economy_Refinery
    #progressive
    ItemData("Progressive Outhouse", ItemClassification.useful, "Prog_Outhouse"), #Type: Building_Outhouse
    #progressive
    ItemData("Progressive Healing Bay", ItemClassification.useful, "Prog_HealingBay"), #Type: Building_HealingBay
    ItemData("Progressive Janitor Station", ItemClassification.useful, "Prog_Janitor"), #Type: Building_JanitorStation
    #progressive
    ItemData("Empowered Shrine of Disciples", ItemClassification.useful, "Building_Shrine_Disciple_Boost"), #Type: Building_Shrine_Disciple_Boost
    ItemData("Cheaper Rituals", ItemClassification.useful, "Temple_CheaperRituals"), #Type: Temple_CheaperRituals
    ItemData("Progressive Shrine Flame", ItemClassification.useful, "Prog_ShrineFlame"), #Type: Shrine_Flame
    ItemData("Confession Booth", ItemClassification.useful, "Building_ConfessionBooth"), #Type: Building_ConfessionBooth
    ItemData("Propaganda Speaker", ItemClassification.filler, "Building_PropagandaSpeakers"), #Type: Building_PropagandaSpeakers
    ItemData("Progressive Crypt", ItemClassification.useful, "Prog_Crypt"), #Type: Building_Crypt_1
    #progressive
    ItemData("Progressive Missionary", ItemClassification.useful, "Prog_Missionary"), #Type: Building_MissionaryII
    ItemData("Progressive Demonic Summoning Circle", ItemClassification.useful, "Prog_DemonSummoner"), #Type: Building_DemonSummoner_2
    ItemData("Fertiliser Silo", ItemClassification.useful, "Building_SiloFertiliser"), #Type: Building_SiloFertiliser
    ItemData("Progressive Harvest Totem", ItemClassification.useful, "Prog_HarvestTotem"), #Type: Building_HarvestTotem

    #Tier 4
    ItemData("Progressive Shrine & Temple Upgrade", ItemClassification.useful, "Prog_Temple"), #Type: TEMPLE_III
    #progressive
    ItemData("Shared Shelter", ItemClassification.useful, "Building_Shared_House"), #Type: Building_Shared_House
    ItemData("Progressive Bed", ItemClassification.useful, "Prog_Bed"), #Type: Building_Beds3
    #progressive bed 3 grand bed
    ItemData("Progressive Janitor Station", ItemClassification.useful, "Prog_Janitor"), #Type: Building_JanitorStation_2
    #progressive
    ItemData("Collected Shrine of Disciples", ItemClassification.useful, "Building_Shrine_Disciple_Collection"), #Type: Building_Shrine_Disciple_Collection
    ItemData("Ritual Cool Downs", ItemClassification.useful, "Temple_FasterCoolDowns"), #Type: Temple_FasterCoolDowns
    ItemData("Progressive Tabernacle", ItemClassification.useful, "Prog_Tabernacle"), #Type: Shrine_PassiveShrinesII
    ItemData("Progressive Shrine Flame", ItemClassification.useful, "Prog_ShrineFlame"), #Type: Shrine_FlameII
    ItemData("Progressive Drink House", ItemClassification.useful, "Prog_Pub"), #Type: Building_Pub
    ItemData("Drum Circle", ItemClassification.useful, "Building_Drum"), #Type: Building_Drum
    ItemData("Mating Tent", ItemClassification.useful, "Building_MatingTent"), #Type: Building_MatingTent
    ItemData("Progressive Hatchery", ItemClassification.useful, "Prog_Hatchery"), #Type: Building_Hatchery
    ItemData("Progressive Crypt", ItemClassification.useful, "Prog_Crypt"), #Type: Building_Crypt_2
    ItemData("Progressive Morgue", ItemClassification.useful, "Prog_Morgue"), #Type: Building_Morgue_1
    ItemData("Progressive Refinery", ItemClassification.progression, "Prog_Refinery"), #Type: Economy_Refinery_2
    ItemData("Bone Decorations", ItemClassification.filler, "Building_Decorations2"), #Type: Building_Decorations2
    ItemData("Progressive Farming Station", ItemClassification.useful, "Prog_FarmStation"), #Type: Building_FarmStationII
    ItemData("Compost", ItemClassification.useful, "Followers_Compost"), #Type: Followers_Compost
    ItemData("Progressive Scarecrow", ItemClassification.useful, "Prog_Scarecrow"), #Type: Building_Scarecrow2
    
    #Tier 5
    ItemData("Progressive Shrine & Temple Upgrade", ItemClassification.useful, "Prog_Temple"), #Type: TEMPLE_IV
    ItemData("Progressive Outhouse", ItemClassification.useful, "Prog_Outhouse"), #Type: Building_Outhouse2
    ItemData("Progressive Healing Bay", ItemClassification.useful, "Prog_HealingBay"), #Type: Building_HealingBay2
    ItemData("Leader Tent", ItemClassification.useful, "Building_LeaderTent"), #Type: Building_LeaderTent
    ItemData("Progressive Tabernacle", ItemClassification.useful, "Prog_Tabernacle"),  #Type: Shrine_PassiveShrinesIII
    ItemData("Progressive Shrine Flame", ItemClassification.useful, "Prog_ShrineFlame"), #Type: Shrine_FlameIII
    ItemData("Progressive Drink House", ItemClassification.useful, "Prog_Pub"), #Type: Building_Pub_2
    ItemData("Re-Indoctrination Stone", ItemClassification.filler, "Building_UpgradedIndoctrination"), #Type: Building_UpgradedIndoctrination
    ItemData("Progressive Hatchery", ItemClassification.useful, "Prog_Hatchery"), #Type: Building_Hatchery_2
    ItemData("Nursery", ItemClassification.useful, "Building_Daycare"), #Type: Building_Daycare
    ItemData("Progressive Crypt", ItemClassification.useful, "Prog_Crypt"), #Type: Building_Crypt_3
    ItemData("Progressive Morgue", ItemClassification.useful, "Prog_Morgue"), #Type: Building_Morgue_2
    ItemData("Progressive Lumberyard", ItemClassification.progression, "Prog_Lumberjack"), #Type: Economy_LumberyardII
    ItemData("Progressive Stone Mine", ItemClassification.progression, "Prog_Mine"), #Type: Economy_MineII
    ItemData("Progressive Missionary", ItemClassification.useful, "Prog_Missionary"),  #Type: Building_MissionaryIII
    ItemData("Progressive Demonic Summoning Circle", ItemClassification.useful, "Prog_DemonSummoner"), #type: Building_DemonSummoner_3
    ItemData("Kitchen", ItemClassification.useful, "Building_Kitchen"), #Type: Building_Kitchen
    ItemData("Fertiliser Storage", ItemClassification.useful, "Building_PoopBucket"), #Type: Building_PoopBucket
    ItemData("Seed Storage", ItemClassification.useful, "Building_SeedBucket"), #Type: Building_SeedBucket
    ItemData("Progressive Harvest Totem", ItemClassification.useful, "Prog_HarvestTotem"), #Type: Building_HarvestTotem2
]