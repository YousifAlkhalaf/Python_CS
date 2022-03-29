import math
import Moves

# Type = attacking type
normal_type = {'ROCK': 0.5, 'STEEL': 0.5, 'GHOST': 0}
fire_type = {'WATER': 0.5, 'GRASS': 2, 'FIRE': 0.5, 'ROCK': 0.5, 'BUG': 2, 'STEEL': 2, 'ICE': 2, 'DRAGON': 0.5}
water_type = {'GROUND': 2, 'ROCK': 2, 'FIRE': 2, 'GRASS': 0.5, 'WATER': 0.5, 'DRAGON': 0.5}
grass_type = {'FLYING': 0.5, 'POISON': 0.5, 'ROCK': 2, 'GROUND': 2, 'BUG': 0.5, 'STEEL': 0.5, 'FIRE': 0.5, 'WATER': 2, 'GRASS': 0.5, 'DRAGON': 0.5}
electric_type = {'FLYING': 2, 'GROUND': 0, 'WATER': 2, 'GRASS': 0.5, 'ELECTRIC': 0.5, 'DRAGON': 0.5}
psychic_type = {'POISON': 2, 'FIGHTING': 2, 'STEEL': 0.5, 'PSYCHIC': 0.5, 'DARK': 0}

type_matchups = {'NORMAL': normal_type, 'FIRE': fire_type, 'WATER': water_type, 'GRASS': grass_type, 'PSYCHIC': psychic_type}


class Pokemon(object):

    def __init__(self):
        pass

    def get_lvl(self):
        return self.lvl

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
        hp = ((2 * base_stat) * level)/100 + level + 10
        return math.ceil(hp)

    # Any other stat of a Pokemon
    def calc_stat(self, base_stat, level):
        stat = ((2 * base_stat) * level)/100 + 5
        return math.ceil(stat)

    # Finds type effectiveness multiplier based on move type.
    def calc_type_effectiveness(self, move_type):
        multiplier = 1
        atk_type = type_matchups[move_type]

        for type in self.types:
            if type in atk_type:
                multiplier *= atk_type[type]
        return multiplier

    def set_moves(self):
        moveset = []
        while len(moveset) < 4:
            for i in range (self.get_lvl(), 0, -1):
                if i in self.learnset:
                    moveset.append(self.learnset[i])
                if len(moveset) >= 4:
                    return moveset
            moveset.append(None)
        return moveset

    def set_status(self, status):
        self.status = status


class Starmie(Pokemon):

    def __init__(self, lvl=100):
        self.lvl = lvl
        self.status = 'OK'

        self.learnset = {1: Moves.Psychic(), 5: Moves.Surf(), 10: Moves.ConfuseRay(), 15: Moves.IceBeam()}

        self.max_hp = self.calc_hp(60, lvl)
        self.hp = self.max_hp
        self.attack = self.calc_stat(75, lvl)
        self.defense = self.calc_stat(85, lvl)
        self.sp_atk = self.calc_stat(100, lvl)
        self.sp_def = self.calc_stat(85, lvl)
        self.speed = self.calc_stat(115, lvl)

        self.types = ('WATER', 'PSYCHIC')
        self.moveset = self.set_moves()

class Venusaur(Pokemon):

    def __init__(self, lvl=100):
        self.lvl = lvl
        self.status = 'OK'

        self.learnset = {1: Moves.EnergyBall(), 5: Moves.PoisonPowder(), 10: Moves.SludgeBomb(), 15: Moves.Rest()}

        self.max_hp = self.calc_hp(80, lvl)
        self.hp = self.max_hp
        self.attack = self.calc_stat(82, lvl)
        self.defense = self.calc_stat(83, lvl)
        self.sp_atk = self.calc_stat(100, lvl)
        self.sp_def = self.calc_stat(100, lvl)
        self.speed = self.calc_stat(80, lvl)

        self.types = ('GRASS', 'POISON')
        self.moveset = self.set_moves()

print(Starmie().moveset)