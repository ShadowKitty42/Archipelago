from ast import Tuple
import typing
from BaseClasses import Item, ItemClassification

class CotLItem(Item):  # or from Items import MyGameItem
    game = "Cult of the Lamb"  # name of the game/world this item is from

class ItemData(Tuple):
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
    #ItemData("Temple", ItemClassification.useful), #Type: TEMPLE
    ItemData("Progressive Bed", ItemClassification.useful, "Prog_Bed"), #Type: BED
    #will need make this a progressive bed due to how its built sleeping bag
    ItemData("Body Pit", ItemClassification.useful, "Building_BodyPit"), #Type: BODY_PIT
    #may need logic due to possibility of killing all base from infection
    ItemData("Farm Plot", ItemClassification.useful, "Building_Farms"), #Type: FARM_PLOT
    #may need to be logic to keep cultists alive to open areas
    ItemData("Progressive Farming Station", ItemClassification.useful, "Prog_FarmStation"), #Type: FARM_STATION
    #may need to be logic to keep cultists alive to open areas
    ItemData("Seed Silo", ItemClassification.useful, "Building_FollowerFarming"), #Type: SILO_SEED
    ItemData("Tailor", ItemClassification.filler, "Building_Tailor"), #Type: TAILOR
    
    #Tier 2
    ItemData("Progressive Shrine & Temple Upgrade", ItemClassification.useful, "Prog_Temple"), #Type: TEMPLE_II
    #Progressive
    ItemData("Basic Decorations", ItemClassification.filler, "Building_Decorations1"), 
    ItemData("Progressive Bed", ItemClassification.useful, "Prog_Bed"), #Type: BED_2
    #Progressive bed 2 shelter
    ItemData("Offering Statue", ItemClassification.useful, "Shrine_OfferingStatue"), #Type: OFFERING_STATUE
    ItemData("Progressive Tabernacle", ItemClassification.useful, "Prog_Tabernacle"), #Type: SHRINE_PASSIVE
    ItemData("Prison", ItemClassification.useful, "Building_Prison"), #Type: PRISON
    ItemData("Progressive Lumberyard", ItemClassification.progression, "Prog_Lumberjack"), #Type: LUMBERJACK_STATION
    ItemData("Progressive Stone Mine", ItemClassification.progression, "Prog_Mine"), #Type: BLOODSTONE_MINE
    #need to check note as I believe bloodstone mine is not what it said before I started the Woolhaven DLC
    ItemData("Progressive Missionary", ItemClassification.useful, "Prog_Missionary"), 
    ItemData("Progressive Demonic Summoning Circle", ItemClassification.useful, "Prog_DemonSummoner"), #Type: DEMON_SUMMONER
    #should also be a progressive item
    ItemData("Progressive Scarecrow", ItemClassification.useful, "Prog_Scarecrow"), #Type: SCARECROW
    
    #Tier 3
    ItemData("Progressive Refinery", ItemClassification.progression, "Prog_Refinery"), #Type: REFINERY
    #progressive
    ItemData("Progressive Outhouse", ItemClassification.useful, "Prog_Outhouse"), #Type: OUTHOUSE
    #progressive
    ItemData("Progressive Healing Bay", ItemClassification.useful, "Prog_HealingBay"), #Type: HEALING_BAY
    ItemData("Progressive Janitor Station", ItemClassification.useful, "Prog_Janitor"), #Type: JANITOR_STATION
    #progressive
    ItemData("Empowered Shrine of Disciples", ItemClassification.useful, "Building_Shrine_Disciple_Boost"), #Type: SHRINE_DISCIPLE_BOOST
    ItemData("Cheaper Rituals", ItemClassification.useful, "Temple_CheaperRituals"), 
    ItemData("Progressive Shrine Flame", ItemClassification.useful, "Prog_ShrineFlame"), 
    ItemData("Confession Booth", ItemClassification.useful, "Building_ConfessionBooth"), #Type: CONFESSION_BOOTH
    ItemData("Propaganda Speaker", ItemClassification.filler, "Building_PropagandaSpeakers"), #Type: PROPAGANDA_SPEAKER
    ItemData("Progressive Crypt", ItemClassification.useful, "Prog_Crypt"), #
    #progressive
    ItemData("Progressive Missionary", ItemClassification.useful, "Prog_Missionary"), 
    ItemData("Progressive Demonic Summoning Circle", ItemClassification.useful, "Prog_DemonSummoner"),
    ItemData("Fertiliser Silo", ItemClassification.useful, "Building_SiloFertiliser"), 
    ItemData("Progressive Harvest Totem", ItemClassification.useful, "Prog_HarvestTotem"), 

    #Tier 4
    ItemData("Progressive Shrine & Temple Upgrade", ItemClassification.useful, "Prog_Temple"), #Type: TEMPLE_III
    #progressive
    ItemData("Shared Shelter", ItemClassification.useful, "Building_Shared_House"), #Type: SHARED_HOUSE
    ItemData("Progressive Bed", ItemClassification.useful, "Prog_Bed"), #Type: BED_3
    #progressive bed 3 grand bed
    ItemData("Progressive Janitor Station", ItemClassification.useful, "Prog_Janitor"), #Type: JANITOR_STATION_2
    #progressive
    ItemData("Collected Shrine of Disciples", ItemClassification.useful, "Building_Shrine_Disciple_Collection"), #Type: SHRINE_DISCIPLE_COLLECTION
    ItemData("Ritual Cool Downs", ItemClassification.useful, "Temple_FasterCoolDowns"), 
    ItemData("Progressive Tabernacle", ItemClassification.useful, "Prog_Tabernacle"), 
    ItemData("Progressive Shrine Flame", ItemClassification.useful, "Prog_ShrineFlame"), 
    ItemData("Progressive Drink House", ItemClassification.useful, "Prog_Pub"), #Type: PUB
    ItemData("Mating Tent", ItemClassification.useful, "Building_MatingTent"),
    ItemData("Progressive Hatchery", ItemClassification.useful, "Prog_Hatchery"),
    ItemData("Progressive Crypt", ItemClassification.useful, "Prog_Crypt"), 
    ItemData("Progressive Morgue", ItemClassification.useful, "Prog_Morgue"),
    ItemData("Progressive Refinery", ItemClassification.progression, "Prog_Refinery"), 
    ItemData("Bone Decorations", ItemClassification.filler, "Building_Decorations2"), 
    ItemData("Progressive Farming Station", ItemClassification.useful, "Prog_FarmStation"), 
    ItemData("Compost", ItemClassification.useful, "Followers_Compost"), #Type: COMPOST_BIN
    ItemData("Progressive Scarecrow", ItemClassification.useful, "Prog_Scarecrow"), #Type: SCARECROW_2
    
    #Tier 5
    ItemData("Progressive Shrine & Temple Upgrade", ItemClassification.useful, "Prog_Temple"), #Type: TEMPLE_IV
    ItemData("Progressive Outhouse", ItemClassification.useful, "Prog_Outhouse"), #Type: OUTHOUSE_2
    ItemData("Progressive Healing Bay", ItemClassification.useful, "Prog_HealingBay"), #Type: HEALING_BAY_2
    ItemData("Leader Tent", ItemClassification.useful, "Building_LeaderTent"), 
    ItemData("Progressive Tabernacle", ItemClassification.useful, "Prog_Tabernacle"), 
    ItemData("Progressive Shrine Flame", ItemClassification.useful, "Prog_ShrineFlame"),
    ItemData("Progressive Drink House", ItemClassification.useful, "Prog_Pub"),
    ItemData("Re-Indoctrination Stone", ItemClassification.filler, "Building_UpgradedIndoctrination"), 
    ItemData("Progressive Hatchery", ItemClassification.useful, "Prog_Hatchery"), 
    ItemData("Nursery", ItemClassification.useful, "Building_Daycare"), 
    ItemData("Progressive Crypt", ItemClassification.useful, "Prog_Crypt"), 
    ItemData("Progressive Morgue", ItemClassification.useful, "Prog_Morgue"), 
    ItemData("Progressive Lumberyard", ItemClassification.progression, "Prog_Lumberjack"),
    ItemData("Progressive Stone Mine", ItemClassification.progression, "Prog_Mine"), 
    ItemData("Progressive Missionary", ItemClassification.useful, "Prog_Missionary"), 
    ItemData("Progressive Demonic Summoning Circle", ItemClassification.useful, "Prog_DemonSummoner"), 
    ItemData("Kitchen", ItemClassification.useful, "Building_Kitchen"), 
    ItemData("Fertiliser Storage", ItemClassification.useful, "Building_PoopBucket"), 
    ItemData("Seed Storage", ItemClassification.useful, "Building_SeedBucket"), 
    ItemData("Progressive Harvest Totem", ItemClassification.useful, "Prog_HarvestTotem"), 
]