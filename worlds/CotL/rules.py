from ast import Dict, List
from BaseClasses import CollectionState

def can_survive(player, state: CollectionState) -> bool:
    return can_farm(player, state) and can_refine_materials(player, state)

def can_farm(player, state: CollectionState) -> bool:
    return state.has("Farm Plot", player)

def can_refine_materials(player, state: CollectionState) -> bool:
    return state.has("Progressive Refinery", player)