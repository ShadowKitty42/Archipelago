
import typing

from BaseClasses import Location

class CotLLocation(Location):  # or from Locations import MyGameLocation
    game = "Cult of the Lamb"  # name of the game/world this location is in

class LocationData:
    locationName : str
    region: str
    def __init__(self, locationName ):
        self.locationName = locationName 
      #  self.region = region

mygame_locations : typing.List[LocationData] = [ 
  
    # Shrine Checks 

    #Tier 1 
    #LocationData("Temple"), #Center
    # Building_Temple  
    LocationData("Sleeping Bags"), #L1
    # Building_Beds  
    LocationData("Body Pit"), #L2
    # Building_BodyPit   
    LocationData("Farm Plot"), #R1
    # Building_Farms    
    LocationData("Farming Bundle 1"), #R2
    # Building_Farms     
    LocationData("Farming Bundle 2"), #R2
    # Building_Farms     
    LocationData("Tailor"), #R3
    # Building_Tailor     

    #Tier 2
    LocationData("Cult II"), #Center
    # Building_Temple2
    LocationData("Basic Decorations"), #L1
    # Building_Temple2
    LocationData("Shelter"), #L2
    # Building_BetterBeds
    LocationData("Offering Statue"), #L3
    # Shrine_OfferingStatue
    LocationData("Tabernacle"), #L4
    # Shrine_PassiveShrines
    LocationData("Prison"),#L5
    #Building_Prison
    LocationData("Lumberyard"), #R1
    # Economy_Lumberyard
    LocationData("Stone Mine"), #R2
    # Economy_Mine
    LocationData("Missionary"), #R3
    # Building_Missionary
    LocationData("Demonic Summoning Circle"), #R4
    # Building_DemonSummoner
    LocationData("Scarecrow"), #R5
    # Building_AdvancedFarming

    #Tier 3
    LocationData("Refinery"), #Center
    # Economy_Refinery
    LocationData("Outhouse"), #L1
    # Building_Outhouse
    LocationData("Healing Bay"), #L2
    # Building_HealingBay
    LocationData("Janitor Station"), #L3
    # Building_JanitorStation
    LocationData("Empowered Shrine of Disciples"), #L4
    # Building_Shrine_Disciple_Boost
    LocationData("Cheaper Rituals"), #L5
    # Temple_CheaperRituals
    LocationData("Shrine Flame Bundle"),#L6
    # Shrine_Flame
    LocationData("Confession Booth"), #L7
    # Building_ConfessionBooth
    LocationData("Propaganda Speakers"), #L8
    # Building_PropagandaSpeakers
    LocationData("Crypt I"), #L9
    # Building_Crypt_1
    LocationData("Missionary II"), #R1
    # Building_MissionaryII
    LocationData("Demonic Summoning Circle II"), #R2
    # Building_DemonSummoner_2
    LocationData("Fertiliser Silo"), #R3
    # Building_SiloFertiliser
    LocationData("Harvest Totem"), #R4
    # Building_HarvestTotem

    #Tier 4
    LocationData("Cult III"), #Center
    # Temple_III
    LocationData("Shared Shelter"), #L1
    # Building_Shared_House
    LocationData("Grand Shelter"), #L2
    # Building_Beds3
    LocationData("Janitor Station II"), #L3
    # Building_JanitorStation_2
    LocationData("Collected Shrine of Disciples"), #L4
    # Building_Shrine_Disciple_Collection
    LocationData("Ritual Cool Downs"), #L5
    # Temple_FasterCoolDowns
    LocationData("Tabernacle II"), #L6
    # Shrine_PassiveShrinesII
    LocationData("Shrine Flame II"), #L7
    # Shrine_FlameII
    LocationData("Drink House"), #L8
    # Building_Pub
    LocationData("Drum Circle"), #L9
    # Building_Drum
    LocationData("Mating Tent 1"), #L10
    # Building_MatingTent
    LocationData("Mating Tent 2"), #L10
    # Building_MatingTent
    LocationData("Crypt II"), #L11
    # Building_Crypt_2
    LocationData("Morgue I"), #L12
    # Building_Morgue_1
    LocationData("Refinery II"), #R1
    # Economy_Refinery_2
    LocationData("Bone Decorations"), #R2
    # Building_Decorations2
    LocationData("Farm Station II"), #R3
    # Building_FarmStationII
    LocationData("Compost"), #R4
    # Followers_Compost
    LocationData("Trap Scarecrow"), #R5
    # Building_Scarecrow2

    #Tier 5
    LocationData("Cult IV"), #Center
    # Temple_IV
    LocationData("Outhouse II"), #L1 
    # Building_Outhouse2
    LocationData("Healing Bay II"), #L2 
    # Building_HealingBay2
    LocationData("Leader Tent"), #L3 
    # Building_LeaderTent
    LocationData("Tabernacle III"), #L4 
    # Shrine_PassiveShrinesIII
    LocationData("Shrine Flame III"), #L5 
    # Shrine_FlameIII
    LocationData("Drinkhouse II"), #L6 
    # Building_Pub_2
    LocationData("Re-Indoctrination Stone"), #L7 
    # Building_UpgradedIndoctrination
    LocationData("Hatchery II"), #L8 
    # Building_Hatchery_2
    LocationData("Nursery"), #L9 
    # Building_Daycare
    LocationData("Crypt III"), #L10 
    # Building_Crypt_3
    LocationData("Morgue II"), #L11 
    # Building_Morgue_2
    LocationData("Lumberyard II"), #R1 
    # Economy_LumberyardII
    LocationData("Stone Mine II"), #R2
    # Economy_MineII
    LocationData("Missionary III"), #R3
    # Building_MissionaryIII
    LocationData("Demonic Summoning Circle III"), #R4
    # Building_DemonSummoner_3
    LocationData("Kitchen"), #R5
    # Building_Kitchen
    LocationData("Fertiliser Storage"), #R6
    # Building_PoopBucket
    LocationData("Seed Storage"), #R7
    # Building_SeedBucket
    LocationData("Devotion Harvest Totem"), #R8
    # Building_HarvestTotem2


]