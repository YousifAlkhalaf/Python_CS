import Pokemon
import random

class Move(object):

    def __init__(self):
        pass

    def damage(self, attacker, defender, multiplier):
        rng_pwr = random.uniform(0.8, 1.0)
        lvl_num = (2 * attacker.get_lvl())/5 + 2
        if self.atk_type == 'SPECIAL':
            atk_def_num = attacker.get_sp_atk()/defender.get_sp_def()
        elif self.atk_type == 'PHYSICAL':
            atk_def_num = attacker.get_atk()/defender.get_def()
        dmg = (lvl_num * self.base_pwr * atk_def_num)/50 + 2
        dmg *= rng_pwr * multiplier