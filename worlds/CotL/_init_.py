
# world/mygame/__init__.py

import typing
from .options import CotLOptions  # the options we defined earlier
from .items import CotLItem, mygame_items  # data used below to add items to the World
from .locations import CotLLocation, mygame_locations  # same as above
from worlds.AutoWorld import World
from BaseClasses import Region, Location, Entrance, Item, RegionType, ItemClassification


class MyGameWorld(World):
    """Insert description of the world/game here."""
    game = "Cult of the Lamb"  # name of the game/world
    options_dataclass = CotLOptions  # options the player can set
    options: CotLOptions  # typing hints for option results
    topology_present = False  # show path to required location checks in spoiler

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    base_id = 666
    # instead of dynamic numbering, IDs could be part of data

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {name: id for
                       id, name in enumerate(mygame_items, base_id)}
    location_name_to_id = {name: id for
                           id, name in enumerate(mygame_locations, base_id)}

    items_by_name = {item.itemName: item for item in mygame_items}

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    # item_name_groups = {
       # "weapons": {"sword", "lance"},
    #}

    def generate_early(self) -> None:
        pass  # nothing to do here for now

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
        self.multiworld.regions.append(menu_region)

        menu_region.add_locations(mygame_locations, CotLLocation)

    def create_items(self) -> None:
        for item in map(self.create_item, mygame_items):
            self.multiworld.itempool.append(item)

    def create_item(self, name: str) -> CotLItem:
        item = self.items_by_name[name]
        return CotLItem(item.itemName, item.progression, self.item_name_to_id[name], self.player)