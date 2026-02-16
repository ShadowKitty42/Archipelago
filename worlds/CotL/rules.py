from ast import Dict, List
from BaseClasses import CollectionState

def can_refine_materials(player, state: CollectionState) -> bool:
    return state.has("Progressive Refinery", player)