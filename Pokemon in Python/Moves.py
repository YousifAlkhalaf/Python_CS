import random

class Move(object):

    def __init__(self):
        self.accuracy = 100
        pass

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def calc_damage(self, attacker, defender, multiplier):
        rng_pwr = random.uniform(0.8, 1.0)
        lvl_num = (2 * attacker.get_lvl())/5 + 2
        if self.category == 'STATUS':
            return 0
        elif self.category == 'SPECIAL':
            atk_def_num = attacker.get_sp_atk()/defender.get_sp_def()
        elif self.category == 'PHYSICAL':
            atk_def_num = attacker.get_atk()/defender.get_def()
        dmg = (lvl_num * self.base_pwr * atk_def_num)/50 + 2
        dmg *= rng_pwr * multiplier
        return dmg

    def move_effect(self):
        pass

class Psychic(Move):

    def __init__(self):
        self.base_pwr = 90
        self.name = 'Psychic'
        self.category = 'SPECIAL'
        self.type = 'PSYCHIC'

class Surf(Move):

    def __init__(self):
        self.base_pwr = 90
        self.name = 'Surf'
        self.category = 'SPECIAL'
        self.type = 'WATER'

class ConfuseRay(Move):

    def __init__(self):
        self.name = 'Confuse Ray'
        self.category = 'STATUS'
        self.type = 'GHOST'

    def move_effect(self, pkmn):
        pkmn.set_status('CONFUSED')