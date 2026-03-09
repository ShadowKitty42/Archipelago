
import typing

from BaseClasses import Location

class CotLLocation(Location):  # or from Locations import MyGameLocation
    game = "Cult of the Lamb"  # name of the game/world this location is in

class LocationData:
    locationName : str
    old_name: str
    original_item: str
    menu_name: str
    tier: int
    position: str
    region: str
    def __init__(self, old_name, original_item, menu_name, tier, position ):
        self.locationName = f"{menu_name} Tier{tier} {position}"
        self.old_name = old_name
        self.menu_name = menu_name
        self.original_item = original_item
        self.tier = tier
        self.position = position
      #  self.region = region

mygame_locations : typing.List[LocationData] = [ 
  
    # Shrine Checks 

    #Tier 1 
    #LocationData("Temple"), #Center
    # Building_Temple  
    LocationData("Sleeping Bags", "Building_Beds", "Shrine", 1, "L1"), #L1
    # Building_Beds  
    LocationData("Body Pit", "Building_BodyPit", "Shrine", 1, "L2"), #L2
    # Building_BodyPit   
    LocationData("Farm Plot", "Building_Farms", "Shrine", 1, "R1"), #R1
    # Building_Farms    
    LocationData("Farming Bundle 1", "Building_FollowerFarming", "Shrine", 1, "R2_1"), #R2
    # Building_FollowerFarming    
    LocationData("Farming Bundle 2", "Building_FollowerFarming", "Shrine", 1, "R2_2"), #R2
    # Building_FollowerFarming     
    LocationData("Tailor", "Building_Tailor", "Shrine", 1, "R3"), #R3
    # Building_Tailor     

    #Tier 2
    LocationData("Cult II", "Building_Temple2", "Shrine", 2, "Center"), #Center
    # Building_Temple2
    LocationData("Basic Decorations", "Building_Decorations1", "Shrine", 2, "L1"), #L1
    # Building_Decorations1
    LocationData("Shelter", "Building_BetterBeds", "Shrine", 2, "L2"), #L2
    # Building_BetterBeds
    LocationData("Offering Statue", "Shrine_OfferingStatue", "Shrine", 2, "L3"), #L3
    # Shrine_OfferingStatue
    LocationData("Tabernacle", "Shrine_PassiveShrines", "Shrine", 2, "L4"), #L4
    # Shrine_PassiveShrines
    LocationData("Prison", "Building_Prison", "Shrine", 2, "L5"),#L5
    #Building_Prison
    LocationData("Lumberyard", "Economy_Lumberyard", "Shrine", 2, "R1"), #R1
    # Economy_Lumberyard
    LocationData("Stone Mine", "Economy_Mine", "Shrine", 2, "R2"), #R2
    # Economy_Mine
    LocationData("Missionary", "Building_Missionary", "Shrine", 2, "R3"), #R3
    # Building_Missionary
    LocationData("Demonic Summoning Circle", "Building_DemonSummoner", "Shrine", 2, "R4"), #R4
    # Building_DemonSummoner
    LocationData("Scarecrow", "Building_AdvancedFarming", "Shrine", 2, "R5"), #R5
    # Building_AdvancedFarming

    #Tier 3
    LocationData("Refinery", "Economy_Refinery", "Shrine", 3, "Center"), #Center
    # Economy_Refinery
    LocationData("Outhouse", "Building_Outhouse", "Shrine", 3, "L1"), #L1
    # Building_Outhouse
    LocationData("Healing Bay", "Building_HealingBay", "Shrine", 3, "L2"), #L2
    # Building_HealingBay
    LocationData("Janitor Station", "Building_JanitorStation", "Shrine", 3, "L3"), #L3
    # Building_JanitorStation
    LocationData("Empowered Shrine of Disciples", "Building_Shrine_Disciple_Boost", "Shrine", 3, "L4"), #L4
    # Building_Shrine_Disciple_Boost
    LocationData("Cheaper Rituals", "Temple_CheaperRituals", "Shrine", 3, "L5"), #L5
    # Temple_CheaperRituals
    LocationData("Shrine Flame Bundle", "Shrine_Flame", "Shrine", 3, "L6"),#L6
    # Shrine_Flame
    LocationData("Confession Booth", "Building_ConfessionBooth", "Shrine", 3, "L7"), #L7
    # Building_ConfessionBooth
    LocationData("Propaganda Speakers", "Building_PropagandaSpeakers", "Shrine", 3, "L8"), #L8
    # Building_PropagandaSpeakers
    LocationData("Crypt I", "Building_Crypt_1", "Shrine", 3, "L9"), #L9
    # Building_Crypt_1
    LocationData("Missionary II", "Building_MissionaryII", "Shrine", 3, "R1"), #R1
    # Building_MissionaryII
    LocationData("Demonic Summoning Circle II", "Building_DemonSummoner_2", "Shrine", 3, "R2"), #R2
    # Building_DemonSummoner_2
    LocationData("Fertiliser Silo", "Building_SiloFertiliser", "Shrine", 3, "R3"), #R3
    # Building_SiloFertiliser
    LocationData("Harvest Totem", "Building_HarvestTotem", "Shrine", 3, "R4"), #R4
    # Building_HarvestTotem

    #Tier 4
    LocationData("Cult III", "Temple_III", "Shrine", 4, "Center"), #Center
    # Temple_III
    LocationData("Shared Shelter", "Building_Shared_House", "Shrine", 4, "L1"), #L1
    # Building_Shared_House
    LocationData("Grand Shelter", "Building_Beds3", "Shrine", 4, "L2"), #L2
    # Building_Beds3
    LocationData("Janitor Station II", "Building_JanitorStation_2", "Shrine", 4, "L3"), #L3
    # Building_JanitorStation_2
    LocationData("Collected Shrine of Disciples", "Building_Shrine_Disciple_Collection", "Shrine", 4, "L4"), #L4
    # Building_Shrine_Disciple_Collection
    LocationData("Ritual Cool Downs", "Temple_FasterCoolDowns", "Shrine", 4, "L5"), #L5
    # Temple_FasterCoolDowns
    LocationData("Tabernacle II", "Shrine_PassiveShrinesII", "Shrine", 4, "L6"), #L6
    # Shrine_PassiveShrinesII
    LocationData("Shrine Flame II", "Shrine_FlameII", "Shrine", 4, "L7"), #L7
    # Shrine_FlameII
    LocationData("Drink House", "Building_Pub", "Shrine", 4, "L8"), #L8
    # Building_Pub
    LocationData("Drum Circle", "Building_Drum", "Shrine", 4, "L9"), #L9
    # Building_Drum
    LocationData("Mating Tent 1", "Building_MatingTent", "Shrine", 4, "L10_1"), #L10
    # Building_MatingTent
    LocationData("Mating Tent 2", "Building_MatingTent", "Shrine", 4, "L10_2"), #L10
    # Building_MatingTent
    LocationData("Crypt II", "Building_Crypt_2", "Shrine", 4, "L11"), #L11
    # Building_Crypt_2
    LocationData("Morgue I", "Building_Morgue_1", "Shrine", 4, "L12"), #L12
    # Building_Morgue_1
    LocationData("Refinery II", "Economy_Refinery_2", "Shrine", 4, "R1"), #R1
    # Economy_Refinery_2
    LocationData("Bone Decorations", "Building_Decorations2", "Shrine", 4, "R2"), #R2
    # Building_Decorations2
    LocationData("Farm Station II", "Building_FarmStationII", "Shrine", 4, "R3"), #R3
    # Building_FarmStationII
    LocationData("Compost", "Followers_Compost", "Shrine", 4, "R4"), #R4
    # Followers_Compost
    LocationData("Trap Scarecrow", "Building_Scarecrow2", "Shrine", 4, "R5"), #R5
    # Building_Scarecrow2

    #Tier 5
    LocationData("Cult IV", "Temple_IV", "Shrine", 5, "Center"), #Center
    # Temple_IV
    LocationData("Outhouse II", "Building_Outhouse2", "Shrine", 5, "L1"), #L1 
    # Building_Outhouse2
    LocationData("Healing Bay II", "Building_HealingBay2", "Shrine", 5, "L2"), #L2 
    # Building_HealingBay2
    LocationData("Leader Tent", "Building_LeaderTent", "Shrine", 5, "L3"), #L3 
    # Building_LeaderTent
    LocationData("Tabernacle III", "Shrine_PassiveShrinesIII", "Shrine", 5, "L4"), #L4 
    # Shrine_PassiveShrinesIII
    LocationData("Shrine Flame III", "Shrine_FlameIII", "Shrine", 5, "L5"), #L5 
    # Shrine_FlameIII
    LocationData("Drinkhouse II", "Building_Pub_2", "Shrine", 5, "L6"), #L6 
    # Building_Pub_2
    LocationData("Re-Indoctrination Stone", "Building_UpgradedIndoctrination", "Shrine", 5, "L7"), #L7 
    # Building_UpgradedIndoctrination
    LocationData("Hatchery II", "Building_Hatchery_2", "Shrine", 5, "L8"), #L8 
    # Building_Hatchery_2
    LocationData("Nursery", "Building_Daycare", "Shrine", 5, "L9"), #L9 
    # Building_Daycare
    LocationData("Crypt III", "Building_Crypt_3", "Shrine", 5, "L10"), #L10 
    # Building_Crypt_3
    LocationData("Morgue II", "Building_Morgue_2", "Shrine", 5, "L11"), #L11 
    # Building_Morgue_2
    LocationData("Lumberyard II", "Economy_LumberyardII", "Shrine", 5, "R1"), #R1 
    # Economy_LumberyardII
    LocationData("Stone Mine II", "Economy_MineII", "Shrine", 5, "R2"), #R2
    # Economy_MineII
    LocationData("Missionary III", "Building_MissionaryIII", "Shrine", 5, "R3"), #R3
    # Building_MissionaryIII
    LocationData("Demonic Summoning Circle III", "Building_DemonSummoner_3", "Shrine", 5, "R4"), #R4
    # Building_DemonSummoner_3
    LocationData("Kitchen", "Building_Kitchen", "Shrine", 5, "R5"), #R5
    # Building_Kitchen
    LocationData("Fertiliser Storage", "Building_PoopBucket", "Shrine", 5, "R6"), #R6
    # Building_PoopBucket
    LocationData("Seed Storage", "Building_SeedBucket", "Shrine", 5, "R7"), #R7
    # Building_SeedBucket
    LocationData("Devotion Harvest Totem", "Building_HarvestTotem2", "Shrine", 5, "R8"), #R8
    # Building_HarvestTotem2


]