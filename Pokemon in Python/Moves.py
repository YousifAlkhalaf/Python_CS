import random


class Move(object):

    def __init__(self):
        self.accuracy = 100
        pass

    def __str__(self):
        out_str = self.name
        out_str += '\n\t' + self.type
        out_str += '\n\t' + self.category
        if self.base_pwr != 0:
            out_str += '\n\t' + str(self.base_pwr)
        return out_str

    def __repr__(self):
        return self.__str__()

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def get_base_pwr(self):
        return self.base_pwr

    def calc_damage(self, attacker, defender, multiplier=1):
        rng_pwr = random.randint(85, 100) / 100
        lvl_num = (2 * attacker.get_lvl()) / 5 + 2
        if self.category == 'STATUS':
            return 0
        elif self.category == 'SPECIAL':
            atk_def_num = attacker.get_sp_atk() / defender.get_sp_def()
        elif self.category == 'PHYSICAL':
            atk_def_num = attacker.get_atk() / defender.get_def()
        dmg = (lvl_num * self.base_pwr * atk_def_num) / 50 + 2
        dmg *= rng_pwr
        dmg *= multiplier
        return dmg

    def self_effect(self, target):
        pass

    def foe_effect(self, target):
        pass

    def accuracy_check(self):
        rng_num = random.randint(1, 100)
        if rng_num > self.accuracy:
            return False
        else:
            return True


class SpecialMove(Move):

    def __init__(self):
        super().__init__()
        self.category = 'SPECIAL'


class PhysicalMove(Move):

    def __init__(self):
        super().__init__()
        self.category = 'PHYSICAL'


class StatusMove(Move):

    def __init__(self):
        super().__init__()
        self.category = 'STATUS'
        self.base_pwr = 0

# Used for confusion
class ConfusionMove(PhysicalMove):
    def __init__(self):
        super().__init__()
        self.base_pwr = 40
        self.accuracy = 33


class ConfuseRay(StatusMove):

    def __init__(self):
        super().__init__()
        self.name = 'Confuse Ray'
        self.type = 'GHOST'

    def foe_effect(self, target):
        target.set_status('CONFUSED')
        print(f'{target.get_name()} is now confused!')


class EnergyBall(SpecialMove):

    def __init__(self):
        super().__init__()
        self.base_pwr = 90
        self.name = 'Energy Ball'
        self.type = 'GRASS'


class Flamethrower(SpecialMove):

    def __init__(self):
        super().__init__()
        self.name = 'Flamethrower'
        self.type = 'FIRE'
        self.base_pwr = 90


class IceBeam(SpecialMove):

    def __init__(self):
        super().__init__()
        self.name = 'Ice Beam'
        self.type = 'ICE'
        self.base_pwr = 90


class LovelyKiss(StatusMove):

    def __init__(self):
        super().__init__()
        self.name = 'Lovely Kiss'
        self.type = 'NORMAL'
        self.accuracy = 75

    def foe_effect(self, target):
        target.set_status('SLEEP')
        print(f'{target.get_name()} fell asleep!')


class PoisonPowder(StatusMove):
    def __init__(self):
        super().__init__()
        self.name = 'Poison Powder'
        self.type = 'POISON'
        self.accuracy = 75

    def foe_effect(self, target):
        target.set_status('POISONED')
        print(f'{target.get_name()} is now poisoned!')


class Psychic(SpecialMove):

    def __init__(self):
        super().__init__()
        self.base_pwr = 90
        self.name = 'Psychic'
        self.type = 'PSYCHIC'


class Recover(StatusMove):

    def __init__(self):
        super().__init__()
        self.name = 'Recover'
        self.type = 'NORMAL'

    def self_effect(self, target):
        print(f'{target.get_name()} recovered HP!')
        target.set_hp(target.get_max_hp()/2)


class Rest(StatusMove):

    def __init__(self):
        super().__init__()
        self.name = 'Rest'
        self.type = 'PSYCHIC'

    def self_effect(self, target):
        target.set_hp(target.get_max_hp())
        target.set_status('SLEEP')
        print(f'{target.get_name()} went to sleep and regained all its HP!')


class ShadowBall(SpecialMove):

    def __init__(self):
        super().__init__()
        self.base_pwr = 90
        self.name = 'Shadow Ball'
        self.type = 'GHOST'


class SludgeBomb(SpecialMove):

    def __init__(self):
        super().__init__()
        self.base_pwr = 90
        self.name = 'Sludge Bomb'
        self.type = 'POISON'


class Surf(SpecialMove):

    def __init__(self):
        super().__init__()
        self.base_pwr = 90
        self.name = 'Surf'
        self.type = 'WATER'


print('Moves loaded!')
