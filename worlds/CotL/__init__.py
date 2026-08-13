
# world/mygame/__init__.py

import typing
import threading
from .options import CotLOptions  # the options we defined earlier
from .items import CotLItem, ItemData, mygame_items  # data used below to add items to the World
from .locations import CotLLocation, mygame_locations  # same as above
from worlds.AutoWorld import World
from BaseClasses import Region, Location, Entrance
from .rules import *


class CotLWorld(World):
    """Insert description of the world/game here."""
    game = "Cult of the Lamb"  # name of the game/world
    options_dataclass = CotLOptions  # options the player can set
    options: CotLOptions  # typing hints for option results
    topology_present = False  # show path to required location checks in spoiler
    ap_version = "0.0.0.1"

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    base_id = 666
    # instead of dynamic numbering, IDs could be part of data

    shrine_dict: typing.Dict[str, str]


    slot_data_ready = threading.Event()

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {data.itemName: index for index, data in enumerate(mygame_items, base_id)}
    location_name_to_id = {data.locationName: index for index, data in enumerate(mygame_locations, base_id)}

    items_by_name = {item.itemName: item for item in mygame_items}
    locations_by_name = {location.locationName: location for location in mygame_locations}
    shrine_upgrades = [location.original_item for location in mygame_locations]

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    # item_name_groups = {
       # "weapons": {"sword", "lance"},
    #}

    def generate_early(self) -> None:
        self.shrine_dict = {}

    def create_regions(self) -> None:
        # Create regions here and add them to self.regions
        # Regions can be created manually or loaded from data
        #
        # Example of creating a region manually:
        #
        # region = Region("Region Name", RegionType.Generic, self.player)
        # location = CotLLocation(self.location_name_to_id["Location Name"], "Location Name", region)
        # region.locations.append(location)
        # self.regions.append(region)
        #
        # Example of loading regions from data:
        #
        # for region_data in mygame_regions:
        #     region = Region(region_data.name, RegionType.Generic, self.player)
        #     for location_data in region_data.locations:
        #         location = CotLLocation(self.location_name_to_id[location_data.locationName], location_data.locationName, region)
        #         region.locations.append(location)
        #     self.regions.append(region)

        menu_region = Region("Menu", self.player, self.multiworld)
        for loc in mygame_locations:
            if loc.tier <= 2:
                location = CotLLocation(self.player, loc.locationName, self.location_name_to_id[loc.locationName], menu_region)
                menu_region.locations.append(location)
        self.multiworld.regions.append(menu_region)

        refinery_region = Region("Refinery", self.player, self.multiworld)
        for loc in mygame_locations:
            if loc.tier > 2:
                location = CotLLocation(self.player, loc.locationName, self.location_name_to_id[loc.locationName], menu_region)
                refinery_region.locations.append(location)
        self.multiworld.regions.append(refinery_region)

        menu_region.connect(refinery_region, None, lambda state: can_survive(self.player, state))

    def create_items(self) -> None:
        for item in map(self.create_item, mygame_items):
            self.multiworld.itempool.append(item)

    def post_fill(self):
        location_list = self.multiworld.get_locations(self.player)
        print(location_list)
        for loc in location_list:
            location_data = self.locations_by_name[loc.name]
            if loc.item.player == self.player:
                item_data = self.items_by_name[loc.item.name]
                print(f"{loc.name}, {location_data.original_item}, {loc.item.name}, {item_data.upgrade_name}")
                self.shrine_dict[location_data.original_item] = f"{item_data.upgrade_name}>>{self.player}"
            else:
                self.shrine_dict[location_data.original_item] = f"{loc.item.name}>>{loc.item.player}"

    def generate_output(self, output_directory: str) -> None:
        # This is where you would write any output files needed to run the game with the generated world.
        # This could be a spoiler log, a patch file, or something else. It can also be left empty if
        # no output is needed.
        

        self.slot_data_ready.set()

    def fill_slot_data(self) -> typing.Dict[str, typing.Any]:
        # This is where you would return any data needed to run the game with the generated world.
        # This could be a dictionary of item locations, a list of events, or something else. It can
        # also be left empty if no data is needed.
        self.slot_data_ready.wait()
        slot_data = {
            "APWorld_Version": self.ap_version,
            "AP_seed": str(self.multiworld.seed),
            "AP_slotName": self.multiworld.player_name[self.player],
            "AP_PlayerID": self.player,
            "shrine_dict": self.shrine_dict,
            "item_small": {item.itemName: item.upgrade_name for item in mygame_items},
            "locations": {location.original_item: {"locationName": location.locationName, "old_name": location.old_name} for location in mygame_locations},
            "goal": "collect_poop"
        }
        return slot_data

    def create_item(self, itemName: ItemData) -> CotLItem:
        item = self.items_by_name[itemName.itemName]
        return CotLItem(item.itemName, item.progression, self.item_name_to_id[itemName.itemName], self.player)