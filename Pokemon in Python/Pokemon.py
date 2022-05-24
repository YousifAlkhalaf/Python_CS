import math
import random
import Moves

# Type in name = attacking type
# Types in dict = defending type and multiplier

normal_type = {'ROCK': 0.5, 'GHOST': 0, 'STEEL': 0.5}
fighting_type = {'NORMAL': 2, 'FLYING': 0.5, 'POISON': 0.5, 'ROCK': 2, 'BUG': 0.5,
                 'GHOST': 0, 'STEEL': 2, 'PSYCHIC': 0.5, 'ICE': 2, 'DARK': 2, 'FAIRY': 0.5}
flying_type = {'FIGHTING': 2, 'ROCK': 0.5, 'BUG': 2,
               'STEEL': 0.5, 'GRASS': 2, 'ELECTRIC': 0.5}
poison_type = {'POISON': 0.5, 'GROUND': 0.5, 'ROCK': 0.5,
               'GHOST': 0.5, 'STEEL': 0, 'GRASS': 2, 'FAIRY': 2}
ground_type = {'FLYING': 0, 'POISON': 2, 'ROCK': 2, 'BUG': 0.5,
               'STEEL': 2, 'FIRE': 2, 'GRASS': 0.5, 'ELECTRIC': 2}
rock_type = {'FIGHTING': 0.5, 'FLYING': 2, 'GROUND': 0.5,
             'BUG': 2, 'STEEL': 0.5, 'FIRE': 2, 'ICE': 2}
bug_type = {'FIGHTING': 0.5, 'FLYING': 0.5, 'POISON': 0.5, 'GHOST': 0.5,
            'STEEL': 0.5, 'FIRE': 0.5, 'GRASS': 2, 'PSYCHIC': 2, 'DARK': 2, 'FAIRY': 0.5}
ghost_type = {'NORMAL': 0, 'GHOST': 2, 'PSYCHIC': 2, 'DARK': 0.5}
steel_type = {'ROCK': 2, 'STEEL': 0.5, 'FIRE': 0.5,
              'WATER': 0.5, 'ELECTRIC': 0.5, 'ICE': 2, 'FAIRY': 2}
fire_type = {'WATER': 0.5, 'GRASS': 2, 'FIRE': 0.5,
             'ROCK': 0.5, 'BUG': 2, 'STEEL': 2, 'ICE': 2, 'DRAGON': 0.5}
water_type = {'GROUND': 2, 'ROCK': 2, 'FIRE': 2,
              'GRASS': 0.5, 'WATER': 0.5, 'DRAGON': 0.5}
grass_type = {'FLYING': 0.5, 'POISON': 0.5, 'ROCK': 2, 'GROUND': 2, 'BUG': 0.5,
              'STEEL': 0.5, 'FIRE': 0.5, 'WATER': 2, 'GRASS': 0.5, 'DRAGON': 0.5}
electric_type = {'FLYING': 2, 'GROUND': 0, 'WATER': 2,
                 'GRASS': 0.5, 'ELECTRIC': 0.5, 'DRAGON': 0.5}
psychic_type = {'POISON': 2, 'FIGHTING': 2,
                'STEEL': 0.5, 'PSYCHIC': 0.5, 'DARK': 0}
ice_type = {'FLYING': 2, 'GROUND': 2, 'STEEL': 0.5, 'FIRE': 0.5,
            'WATER': 0.5, 'GRASS': 2, 'ICE': 0.5, 'DRAGON': 2}
dragon_type = {'STEEL': 0.5, 'DRAGON': 2, 'FAIRY': 0}
dark_type = {'FIGHTING': 0.5, 'GHOST': 2,
             'PSYCHIC': 2, 'DARK': 0.5, 'FAIRY': 0.5}
fairy_type = {'FIGHTING': 2, 'POISON': 0.5,
              'STEEL': 0.5, 'FIRE': 0.5, 'DRAGON': 2, 'DARK': 2}

type_map = {'NORMAL': normal_type, 'FIGHTING': fighting_type, 'FLYING': flying_type, 'POISON': poison_type, 'GROUND': ground_type, 'ROCK': rock_type, 'BUG': bug_type, 'GHOST': ghost_type, 'STEEL': steel_type,
            'FIRE': fire_type, 'WATER': water_type, 'GRASS': grass_type, 'ELECTRIC': electric_type, 'PSYCHIC': psychic_type, 'ICE': ice_type, 'DRAGON': dragon_type, 'DARK': dark_type, 'FAIRY': fairy_type}


class Pokemon(object):

    def __init__(self, moveset, lvl=100):
        self.moveset = moveset
        self.lvl = lvl
        self.status = 'OK'
        self.status_ctr = -1
        self.immobilized = False
        pass

    def __str__(self):
        out_str = self.name + f'{self.hp}/{self.max_hp}'.rjust(20)
        out_str += "\n\t" + self.status
        out_str += "\n\t" + self.types[0]
        out_str += "\n\t" + self.types[1]
        return out_str

    def get_name(self):
        return self.name

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

    def get_status(self):
        return self.status

    def get_moves(self):
        return self.moveset

    def is_immobilized(self):
        return self.immobilized

    # Calculates HP stat of Pokemon
    def calc_hp(self, base_stat, level):
        hp = ((2 * base_stat) * level) / 100 + level + 10
        return math.ceil(hp)

    # Any other stat of a Pokemon
    def calc_stat(self, base_stat, level):
        stat = ((2 * base_stat) * level) / 100 + 5
        return math.ceil(stat)

    # For defending Pokemon
    # Finds type effectiveness multiplier based on move type.
    def calc_type_effectiveness(self, move_type):
        multiplier = 1
        atk_type = type_map[move_type]

        for type in self.types:
            if type in atk_type:
                multiplier *= atk_type[type]
        return multiplier

    # Compares speed
    def faster_than(self, other):
        return self.get_spd() >= other.get_spd()

    # Assigns a status condition
    def set_status(self, status):
        self.status = status

    # Figures out if a Pokemon is immobilized by running immobilizing statuses.
    def run_stun_statuses(self):
        self.immobilized = self.sleep() or self.paralysis() or self.confusion()

    # HP value is set to given value.
    def set_hp(self, val):
        if val > self.max_hp:
            self.hp = self.max_hp
        elif val < 0:
            self.hp = 0
        else:
            self.hp = int(val)

    def lose_hp(self, val):
        self.set_hp(self.hp - val)

    def gain_hp(self, val):
        self.set_hp(self.hp + val)

    # Sleep status logic. Pokemon is asleep and unable to act for 1-3 turns, then wakes up and can act again
    def sleep(self):
        if self.status == 'SLEEP':
            if self.status_ctr == 0:  # Sleep ends
                self.status = 'OK'
                self.status_ctr = -1
                print(f'{self.name} has woken up!')
                return False
            elif self.status_ctr == -1:  # Sleep begins
                self.status_ctr == random.randint(1, 3)
            print(f'{self.name} is asleep!')
            self.status_ctr -= 1
            return True
        else:
            return False  # Pokemon is not asleep

    # Paralysis status logic. Pokemon is paralyzed, has 1 in 4 chance of not being able to use a move
    def paralysis(self):
        if self.status == 'PARALYZED':
            randnum = random.randint(1, 4)  # 25% chance to be paralyzed
            if randnum == 1:
                print('{self.name} is paralyzed! It can\'t move!')
                return True
            return False
        else:
            return False

    # Poison status logic. Pokemon is poisoned, loses 1/16 of max HP
    def poison(self):
        if self.status == 'POISONED':
            print(f'{self.name} is poisoned! It lost HP!')
            self.lose_hp(int(self.max_hp/16))

    # If the Pokemon has fainted
    def has_fainted(self):
        if self.hp == 0:
            print(f'{self.name} has fainted!')
            self.status = 'FAINTED'
            return True
        return False

    # Confusion status logic. Pokemon is confused for 2-5 turns, 1/3 chance to hit itself and not move.
    def confusion(self):
        if self.status == 'CONFUSED':  # Counts down confusion
            if self.status_ctr == 0:  # Confusion ends
                self.status = 'OK'
                self.status_ctr = -1
                print(f'{self.name} has snapped out of its confusion!')
                return False
            elif self.status_ctr == -1:  # Confusion begins
                self.status_ctr == random.randint(2, 5)
            print(f'{self.name} is confused!')

            # Whether or not confusion damage will be dealt.
            # Used to deal confusion damage and decide when to activate
            confuse_move = Moves.ConfusionMove()
            if confuse_move.accuracy_check():
                print('It hit itself in its confusion!')
                # Hits itself.
                self.lose_hp(confuse_move.calc_damage(self, self))
                return True

            self.status_ctr -= 1
            return False
        else:
            return False  # Not confused


class Garchomp(Pokemon):

    def __init__(self, moveset, lvl=100):
        super().__init__(moveset, lvl)
        self.name = 'Garchomp'

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
        self.name = 'Jynx'

        self.max_hp = self.calc_hp(65, lvl)
        self.hp = self.max_hp
        self.attack = self.calc_stat(50, lvl)
        self.defense = self.calc_stat(35, lvl)
        self.sp_atk = self.calc_stat(115, lvl)
        self.sp_def = self.calc_stat(95, lvl)
        self.speed = self.calc_stat(95, lvl)

        self.types = ('ICE', 'PSYCHIC')


class Scrafty(Pokemon):

    def __init__(self, moveset, lvl=100):
        super().__init__(moveset, lvl)
        self.name = 'Scrafty'

        self.max_hp = self.calc_hp(65, lvl)
        self.hp = self.max_hp
        self.attack = self.calc_stat(90, lvl)
        self.defense = self.calc_stat(115, lvl)
        self.sp_atk = self.calc_stat(45, lvl)
        self.sp_def = self.calc_stat(115, lvl)
        self.speed = self.calc_stat(58, lvl)

        self.types = ('DARK', 'FIGHTING')


class Snorlax(Pokemon):

    def __init__(self, moveset, lvl=100):
        super().__init__(moveset, lvl)
        self.name = 'Snorlax'

        self.max_hp = self.calc_hp(160, lvl)
        self.hp = self.max_hp
        self.attack = self.calc_stat(110, lvl)
        self.defense = self.calc_stat(65, lvl)
        self.sp_atk = self.calc_stat(65, lvl)
        self.sp_def = self.calc_stat(110, lvl)
        self.speed = self.calc_stat(30, lvl)

        self.types = ('NORMAL',)


class Starmie(Pokemon):

    def __init__(self, moveset, lvl=100):
        super().__init__(moveset, lvl)
        self.name = 'Starmie'

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
        self.name = 'Venusaur'

        self.max_hp = self.calc_hp(80, lvl)
        self.hp = self.max_hp
        self.attack = self.calc_stat(82, lvl)
        self.defense = self.calc_stat(83, lvl)
        self.sp_atk = self.calc_stat(100, lvl)
        self.sp_def = self.calc_stat(100, lvl)
        self.speed = self.calc_stat(80, lvl)

        self.types = ('GRASS', 'POISON')


print('Pokemon loaded!')
