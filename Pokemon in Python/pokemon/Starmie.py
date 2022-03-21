import Pokemon as Pokemon

import Pokemon

class Starmie(Pokemon):

    def __init__(self, lvl):
        self.max_hp = Pokemon.calc_hp(60, lvl)
        self.attack = Pokemon.calc_stat(75, lvl)
        self.defense = Pokemon.calc_stat(85, lvl)
        self.sp_atk = Pokemon.calc_stat(100, lvl)
        self.sp_def = Pokemon.calc_stat(85, lvl)
        self.speed = Pokemon.calc_stat(115, lvl)

        self.type1 = 'WATER'
        self.type2 = 'PSYCHIC'
