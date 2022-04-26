import math
import Moves

# Type = attacking type
normal_type = {'ROCK': 0.5, 'STEEL': 0.5, 'GHOST': 0}
fire_type = {'WATER': 0.5, 'GRASS': 2, 'FIRE': 0.5, 'ROCK': 0.5, 'BUG': 2, 'STEEL': 2, 'ICE': 2, 'DRAGON': 0.5}
water_type = {'GROUND': 2, 'ROCK': 2, 'FIRE': 2, 'GRASS': 0.5, 'WATER': 0.5, 'DRAGON': 0.5}
grass_type = {'FLYING': 0.5, 'POISON': 0.5, 'ROCK': 2, 'GROUND': 2, 'BUG': 0.5, 'STEEL': 0.5, 'FIRE': 0.5, 'WATER': 2,
              'GRASS': 0.5, 'DRAGON': 0.5}
electric_type = {'FLYING': 2, 'GROUND': 0, 'WATER': 2, 'GRASS': 0.5, 'ELECTRIC': 0.5, 'DRAGON': 0.5}
psychic_type = {'POISON': 2, 'FIGHTING': 2, 'STEEL': 0.5, 'PSYCHIC': 0.5, 'DARK': 0}

type_matchups = {'NORMAL': normal_type, 'FIRE': fire_type, 'WATER': water_type, 'GRASS': grass_type,
                 'PSYCHIC': psychic_type, 'ELECTRIC': electric_type}


class Pokemon(object):

    def __init__(self, moveset, lvl=100):
        self.moveset = moveset
        self.lvl = lvl
        pass

    def __str__(self):
        return str(self.moveset)

    def get_lvl(self):
        return self.lvl

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_atk(self):
        return self.attack

    def get_def(self):
        return self.defense

    def get_sp_atk(self):
        return self.sp_atk

    def get_sp_def(self):
        return self.sp_def

    def get_spd(self):
        return self.speed

    # Calculates HP stat of Pokemon
    def calc_hp(self, base_stat, level):
        hp = ((2 * base_stat) * level) / 100 + level + 10
        return math.ceil(hp)

    # Any other stat of a Pokemon
    def calc_stat(self, base_stat, level):
        stat = ((2 * base_stat) * level) / 100 + 5
        return math.ceil(stat)

    # Finds type effectiveness multiplier based on move type.
    def calc_type_effectiveness(self, move_type):
        multiplier = 1
        atk_type = type_matchups[move_type]

        for type in self.types:
            if type in atk_type:
                multiplier *= atk_type[type]
        return multiplier

    def set_status(self, status):
        self.status = status

    def set_hp(self, val):
        if val > self.max_hp:
            self.hp = self.max_hp
        elif val < 0:
            self.hp = 0
        else:
            self.hp = val


class Starmie(Pokemon):

    def __init__(self, moveset, lvl=100):
        super().__init__(moveset, lvl)
        self.status = 'OK'

        self.max_hp = self.calc_hp(60, lvl)
        self.hp = self.max_hp
        self.attack = self.calc_stat(75, lvl)
        self.defense = self.calc_stat(85, lvl)
        self.sp_atk = self.calc_stat(100, lvl)
        self.sp_def = self.calc_stat(85, lvl)
        self.speed = self.calc_stat(115, lvl)

        self.types = ('WATER', 'PSYCHIC')


class Venusaur(Pokemon):

    def __init__(self, moveset, lvl=100):
        super().__init__(moveset, lvl)
        self.status = 'OK'

        self.max_hp = self.calc_hp(80, lvl)
        self.hp = self.max_hp
        self.attack = self.calc_stat(82, lvl)
        self.defense = self.calc_stat(83, lvl)
        self.sp_atk = self.calc_stat(100, lvl)
        self.sp_def = self.calc_stat(100, lvl)
        self.speed = self.calc_stat(80, lvl)

        self.types = ('GRASS', 'POISON')

class Garchomp(Pokemon):
    
    def __init__(self, moveset, lvl=100):
        super().__init__(moveset, lvl)
        self.status = 'OK'

        self.max_hp = self.calc_hp(108, lvl)
        self.hp = self.max_hp
        self.attack = self.calc_stat(130, lvl)
        self.defense = self.calc_stat(95, lvl)
        self.sp_atk = self.calc_stat(80, lvl)
        self.sp_def = self.calc_stat(85, lvl)
        self.speed = self.calc_stat(102, lvl)

        self.types = ('DRAGON', 'GROUND')

class Jynx(Pokemon):
    
    def __init__(self, moveset, lvl=100):
        super().__init__(moveset, lvl)
        self.status = 'OK'
        
        self.max_hp = self.calc_hp(65, lvl)
        self.hp = self.max_hp
        self.attack = self.calc_stat(50, lvl)
        self.defense = self.calc_stat(35, lvl)
        self.sp_atk = self.calc_stat(115, lvl)
        self.sp_def = self.calc_stat(95, lvl)
        self.speed = self.calc_stat(95, lvl)

        self.types = ('ICE', 'PSYCHIC')
        


print(Starmie([Moves.IceBeam(), Moves.Psychic(), Moves.ConfuseRay(), Moves.Surf()]))
