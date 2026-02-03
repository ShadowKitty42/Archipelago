from BaseClasses import Item, ItemClassification

class CotLItem(Item):  # or from Items import MyGameItem
    game = "Cult of the Lamb"  # name of the game/world this item is from


class ItemData:
    itemName: str
    progression: ItemClassification
    def __init__(self, itemName, progression):
        self.itemName = itemName
        self.progression = progression


mygame_items: typing.List[ItemData] = [

 # Shrine Items 

    #Tier 1 
    ItemData("Temple", ItemClassification.useful), #Type: TEMPLE
    ItemData("Progressive Bed", ItemClassification.useful), #Type: BED
    #will need make this a progressive bed due to how its built sleeping bag
    ItemData("Body Pit", ItemClassification.useful), #Type: BODY_PIT
    #may need logic due to possibility of killing all base from infection
    ItemData("Farm Plot", ItemClassification.useful), #Type: FARM_PLOT
    #may need to be logic to keep cultists alive to open areas
    ItemData("Progressive Farming Station", ItemClassification.useful), #Type: FARM_STATION
    #may need to be logic to keep cultists alive to open areas
    ItemData("Seed Silo", ItemClassification.useful), #Type: SILO_SEED
    ItemData("Tailor", ItemClassification.filler), #Type: TAILOR
    
    #Tier 2
    ItemData("Progressive Shrine & Temple Upgrade", ItemClassification.useful), #Type: TEMPLE_II
    #Progressive
    ItemData("Basic Decorations", ItemClassification.filler), 
    ItemData("Progressive Bed", ItemClassification.useful), #Type: BED_2
    #Progressive bed 2 shelter
    ItemData("Offering Statue", ItemClassification.useful), #Type: OFFERING_STATUE
    ItemData("Progressive Tabernacle", ItemClassification.useful), #Type: SHRINE_PASSIVE
    ItemData("Prison", ItemClassification.useful), #Type: PRISON
    ItemData("Progressive Lumberyard", ItemClassification.progression), #Type: LUMBERJACK_STATION
    ItemData("Progressive Stone Mine", ItemClassification.progression), #Type: BLOODSTONE_MINE
    #need to check note as I believe bloodstone mine is not what it said before I started the Woolhaven DLC
    ItemData("Progressive Missionary", ItemClassification.useful), 
    ItemData("Progressive Demonic Summoning Circle", ItemClassification.useful), #Type: DEMON_SUMMONER
    #should also be a progressive item
    ItemData("Progressive Scarecrow", ItemClassification.useful), #Type: SCARECROW
    
    #Tier 3
    ItemData("Progressive Refinery", ItemClassification.progression), #Type: REFINERY
    #progressive
    ItemData("Progressive Outhouse", ItemClassification.useful), #Type: OUTHOUSE
    #progressive
    ItemData("Progressive Healing Bay", ItemClassification.useful), #Type: HEALING_BAY
    ItemData("Progressive Janitor Station", ItemClassification.useful), #Type: JANITOR_STATION
    #progressive
    ItemData("Empowered Shrine of Disciples", ItemClassification.useful), #Type: SHRINE_DISCIPLE_BOOST
    ItemData("Cheaper Rituals", ItemClassification.useful), 
    ItemData("Progressive Shrine Flame", ItemClassification.useful), 
    ItemData("Confession Booth", ItemClassification.useful), #Type: CONFESSION_BOOTH
    ItemData("Propoganda Speaker"), #Type: PROPAGANDA_SPEAKER
    ItemData("Progressive Crypt", ItemClassification.useful), #
    #progressive
    ItemData("Progressive Missionary", ItemClassification.useful), 
    ItemData("Progressive Demonic Summoning Circle", ItemClassification.useful),
    ItemData("Fertiliser Silo", ItemClassification.useful), 
    ItemData("Progressive Harvest Totem", ItemClassification.useful), 

    #Tier 4
    ItemData("Progressive Temple & Shrine Upgrade", ItemClassification.useful), #Type: TEMPLE_III
    #progressive
    ItemData("Shared Shelter", ItemClassification.useful), #Type: SHARED_HOUSE
    ItemData("Progressive Bed", ItemClassification.useful), #Type: BED_3
    #progressive bed 3 grand bed
    ItemData("Progressive Janitor Station", ItemClassification.useful), #Type: JANITOR_STATION_2
    #progressive
    ItemData("Collected Shrine of Disciples", ItemClassification.useful), #Type: SHRINE_DISCIPLE_COLLECTION
    ItemData("Ritual Cool Downs", ItemClassification.useful), 
    ItemData("Progressive Tabernacle", ItemClassification.useful), 
    ItemData("Progressive Shrine Flame", ItemClassification.useful), 
    ItemData("Progressive Drink House", ItemClassification.useful), #Type: PUB
    ItemData("Mating Tent", ItemClassification.useful), 
    ItemData("Progressive Hatchery", ItemClassification.useful), 
    ItemData("Progressive Crypt", ItemClassification.useful), 
    ItemData("Progressive Morgue", ItemClassification.useful), 
    ItemData("Progressive Refinery", ItemClassification.progression), 
    ItemData("Bone Decorations", ItemClassification.filler), 
    ItemData("Progressive Farming Station", ItemClassification.useful), 
    ItemData("Compost", ItemClassification.useful), #Type: COMPOST_BIN
    ItemData("Progressive Scarecrow", ItemClassification.useful), #Type: SCARECROW_2
    
    #Tier 5
    ItemData("Progressive Temple & Shrine Upgrade", ItemClassification.useful), #Type: TEMPLE_IV
    ItemData("Progressive Outhouse", ItemClassification.useful), #Type: OUTHOUSE_2
    ItemData("Progressive Healing Bay", ItemClassification.useful), #Type: HEALING_BAY_2
    ItemData("Leader Tent", ItemClassification.useful), 
    ItemData("Progressive Tabernacle", ItemClassification.useful), 
    ItemData("Progressive Shrine Flame", ItemClassification.useful),
    ItemData("Progressive Drink House", ItemClassification.useful),
    ItemData("Re-Indoctrination Stone", ItemClassification.filler), 
    ItemData("Progressive Hatchery", ItemClassification.useful), 
    ItemData("Nursery", ItemClassification.useful), 
    ItemData("Progressive Crypt", ItemClassification.useful), 
    ItemData("Progressive Morgue", ItemClassification.useful), 
    ItemData("Progressive Lumberyard", ItemClassification.progression),
    ItemData("Progressive Stone Mine", ItemClassification.progression), 
    ItemData("Progressive Missionary", ItemClassification.useful), 
    ItemData("Progressive Demonic Summoning Circle", ItemClassification.useful), 
    ItemData("Kitchen", ItemClassification.useful), 
    ItemData("Fertiliser Storage", ItemClassification.useful), 
    ItemData("Seed Storage", ItemClassification.useful), 
    ItemData("Progressive Harvest Totem", ItemClassification.useful), 
]