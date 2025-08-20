from enum import Enum


class Sequence_State(Enum):
    EMPTY = 0
    ATTACKS = 1
    HIT = 2
    WOUND = 3
    SAVE = 4
    DAMAGE = 5
    PAIN = 6
