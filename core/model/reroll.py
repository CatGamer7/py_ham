from enum import Enum


class Reroll(Enum):
    NO = 0
    ONES = 1
    FULL = 2

    def __str__(self):
        match self:
            case Reroll.NO:
                return ""

            case Reroll.ONES:
                return " r1"
            
            case Reroll.FULL:
                return " r"
