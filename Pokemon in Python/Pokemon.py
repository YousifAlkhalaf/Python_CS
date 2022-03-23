import math

# Type = attacking type
normal_type = {'ROCK': 0.5, 'STEEL': 0.5, 'GHOST': 0}
fire_type = {'WATER': 0.5, 'GRASS': 2, 'FIRE': 0.5, 'ROCK': 0.5, 'BUG': 2, 'STEEL': 2, 'ICE': 2, 'DRAGON': 0.5}
water_type = {'GROUND': 2, 'ROCK': 2, 'FIRE': 2, 'GRASS': 0.5, 'WATER': 0.5, 'DRAGON': 0.5}
psychic_type = {'POISON': 2, 'FIGHTING': 2, 'STEEL': 0.5, 'PSYCHIC': 0.5, 'DARK': 0}


class Pokemon(object):

    def __init__(self):
        pass

    def calc_hp(self, base_stat, level):
        hp = ((2 * base_stat) * level)/100 + level + 10
        return math.ceil(hp)

    def calc_stat(self, base_stat, level):
        stat = ((2 * base_stat) * level)/100 + 5
        return math.ceil(stat)

    def calc_type_effectiveness(self, move_type):
        multiplier = 1
        if move_type == 'NORMAL':
            atk_type = normal_type
        elif move_type == 'PSYCHIC':
            atk_type = psychic_type
        elif move_type == 'WATER':
            atk_type = 'WATER'
        elif move_type == 'FIRE':
            atk_type = fire_type

        if self.type1 in atk_type:
            multiplier *= atk_type[self.type1]
        if self.type2 in atk_type:
            multiplier *= atk_type[self.type2]
        return multiplier

class Starmie(Pokemon):

    def __init__(self, lvl=100):
        self.max_hp = self.calc_hp(60, lvl)
        self.attack = self.calc_stat(75, lvl)
        self.defense = self.calc_stat(85, lvl)
        self.sp_atk = self.calc_stat(100, lvl)
        self.sp_def = self.calc_stat(85, lvl)
        self.speed = self.calc_stat(115, lvl)
        self.hp = self.max_hp

        self.type1 = 'WATER'
        self.type2 = 'PSYCHIC'

print(Starmie(100).calc_type_effectiveness('PSYCHIC'))