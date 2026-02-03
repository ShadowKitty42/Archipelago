# options.py
from dataclasses import dataclass

from Options import Toggle, Range, Choice, PerGameCommonOptions



class Goal(Choice):
    """Sets goal for the game."""
    display_name = "Goal"
    option_win = 0
    default = 0  # default to normal


@dataclass
class CotLOptions(PerGameCommonOptions):
    goal: Goal
 
