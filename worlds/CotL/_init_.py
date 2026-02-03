
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
    topology_present = True  # show path to required location checks in spoiler

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

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    # item_name_groups = {
       # "weapons": {"sword", "lance"},
    #}