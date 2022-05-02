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
        lvl_num = (2 * attacker.get_lvl()) / 5 + 2
        if self.category == 'STATUS':
            return 0
        elif self.category == 'SPECIAL':
            atk_def_num = attacker.get_sp_atk() / defender.get_sp_def()
        elif self.category == 'PHYSICAL':
            atk_def_num = attacker.get_atk() / defender.get_def()
        dmg = (lvl_num * self.base_pwr * atk_def_num) / 50 + 2
        dmg *= rng_pwr * multiplier
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
    
    def get_type(self):
        return self.type


class SpecialMove(Move):

    def __init__(self):
        self.category = 'SPECIAL'


class PhysicalMove(Move):

    def __init__(self):
        self.category = 'PHYSICAL'


class StatusMove(Move):

    def __init__(self):
        self.category = 'STATUS'


class ConfuseRay(StatusMove):

    def __init__(self):
        self.name = 'Confuse Ray'
        self.type = 'GHOST'

    def foe_effect(self, target):
        target.set_status('CONFUSED')


class EnergyBall(SpecialMove):

    def __init__(self):
        self.base_pwr = 90
        self.name = 'Energy Ball'
        self.type = 'GRASS'


class Flamethrower(SpecialMove):

    def __init__(self):
        self.name = 'Flamethrower'
        self.type = 'FIRE'
        self.base_pwr = 90


class IceBeam(SpecialMove):

    def __init__(self):
        self.name = 'Ice Beam'
        self.type = 'ICE'
        self.base_pw = 90


class LovelyKiss(StatusMove):
    
    def __init__(self):
        self.name = 'Lovely Kiss'
        self.type = 'ICE'
        self.accuracy = 75
    
    def foe_effect(self, target):
        target.set_status('SLEEP')
        
        
class PoisonPowder(StatusMove):
    def __init__(self):
        self.name = 'Poison Powder'
        self.type = 'POISON'
        self.accuracy = 75

    def foe_effect(self, target):
        target.set_status('POISONED')


class Psychic(SpecialMove):

    def __init__(self):
        self.base_pwr = 90
        self.name = 'Psychic'
        self.type = 'PSYCHIC'


class Recover(StatusMove):
    
    def __init__(self):
        self.name = 'Recover'
        self.type = 'Normal'

    def self_effect(self, target):
        target.set_hp(target.get_max_hp()/2)
        
    
class Rest(StatusMove):

    def __init__(self):
        self.name = 'Rest'
        self.type = 'PSYCHIC'

    def self_effect(self, target):
        target.set_hp(target.get_max_hp())
        target.set_status('SLEEP')


class ShadowBall(SpecialMove):
    
    def __init__(self):
        self.base_pwr = 90
        self.name = 'Shadow Ball'
        self.type = 'GHOST'
        
    
class SludgeBomb(SpecialMove):
    
    def __init__(self):
        self.base_pwr = 90
        self.name = 'Sludge Bomb'
        self.type = 'POISON'


class Surf(SpecialMove):

    def __init__(self):
        self.base_pwr = 90
        self.name = 'Surf'
        self.type = 'WATER'

print('Moves loaded!')