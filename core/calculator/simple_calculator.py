from core.model import Attacker, Defender, Reroll
from core.model.value import Non_Positive_Value, Random_Value, Simple_Value


class Simple_Calculator:

    attacker: Attacker
    defender: Defender

    def __init__(self, in_attacker: Attacker, in_defender: Defender):
        self.attacker = in_attacker
        self.defender = in_defender

    def determine_attacks(self, in_reroll: Reroll):
        attacks = self.attacker.attacks

        if isinstance(attacks, Simple_Value):
            pass


    def hit(self, in_reroll: Reroll):
        if self.attacker:
            pass
        
