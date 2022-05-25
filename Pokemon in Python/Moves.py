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

    # Calculates damage based on Pokemon stats and type multiplier.
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
        dmg = int(dmg)
        if dmg != 0:
            print(f'{defender.get_name()} took {dmg} damage!')
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


class BodySlam(PhysicalMove):

    def __init__(self):
        super().__init__()
        self.base_pwr = 85
        self.name = 'Body Slam'
        self.type = 'NORMAL'

    def foe_effect(self, target):
        if random.randint(1, 100) <= 30:
            target.set_status('PARALYZED')
            print(f'{target.get_name()} was paralyzed!')


class ConfuseRay(StatusMove):

    def __init__(self):
        super().__init__()
        self.name = 'Confuse Ray'
        self.type = 'GHOST'

    def foe_effect(self, target):
        target.set_status('CONFUSED')
        print(f'{target.get_name()} became confused!')


class Crunch(PhysicalMove):

    def __init__(self):
        super().__init__()
        self.name = 'Crunch'
        self.type = 'DARK'
        self.base_pwr = 80


class DragonClaw(PhysicalMove):

    def __init__(self):
        super().__init__()
        self.name = 'Dragon Claw'
        self.type = 'DRAGON'
        self.base_pwr = 80


class Earthquake(PhysicalMove):

    def __init__(self):
        super().__init__()
        self.name = 'Earthquake'
        self.type = 'GROUND'
        self.base_pwr = 100


class EnergyBall(SpecialMove):

    def __init__(self):
        super().__init__()
        self.base_pwr = 90
        self.name = 'Energy Ball'
        self.type = 'GRASS'


class FirePunch(PhysicalMove):

    def __init__(self):
        super().__init__()
        self.base_pwr = 75
        self.name = 'Fire Punch'
        self.type = 'FIRE'

    def foe_effect(self, target):
        if random.randint(1, 100) <= 10:
            target.set_status('BURNED')
            print(f'{target.get_name()} is now burned!')


class HighJumpKick(PhysicalMove):

    def __init__(self):
        super().__init__()
        self.name = 'High Jump Kick'
        self.type = 'FIGHTING'
        self.base_pwr = 130
        self.accuracy = 90
        self.has_missed = False

    def accuracy_check(self):
        rng_num = random.randint(1, 100)
        if rng_num > self.accuracy:
            self.has_missed = True
            return False
        else:
            self.has_missed = False
            return True

    def self_effect(self, target):  # Crash damage if the move misses
        if self.has_missed:
            target.lose_hp(target.get_max_hp() / 12)
            print(f'{target.get_name()} crashed and took damage!')


class IceBeam(SpecialMove):

    def __init__(self):
        super().__init__()
        self.name = 'Ice Beam'
        self.type = 'ICE'
        self.base_pwr = 90


class IronHead(PhysicalMove):

    def __init__(self):
        super().__init__()
        self.name = 'Iron Head'
        self.type = 'STEEL'
        self.base_pwr = 80


class LovelyKiss(StatusMove):

    def __init__(self):
        super().__init__()
        self.name = 'Lovely Kiss'
        self.type = 'NORMAL'
        self.accuracy = 75

    def foe_effect(self, target):
        target.set_status('SLEEP')
        print(f'{target.get_name()} fell asleep!')


class PoisonJab(PhysicalMove):

    def __init__(self):
        super().__init__()
        self.name = 'Poison Jab'
        self.type = 'POISON'
        self.base_pwr = 80

    def foe_effect(self, target):
        if random.randint(1, 100) <= 30:
            target.set_status('POISONED')
            print(f'{target.get_name()} is now poisoned!')


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
        target.set_hp(target.get_max_hp() / 2)


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


class ShadowClaw(PhysicalMove):

    def __init__(self):
        super().__init__()
        self.base_pwr = 75
        self.name = 'Shadow Claw'
        self.type = 'GHOST'


class SludgeBomb(SpecialMove):

    def __init__(self):
        super().__init__()
        self.base_pwr = 90
        self.name = 'Sludge Bomb'
        self.type = 'POISON'

    def foe_effect(self, target):
        if random.randint(1, 100) <= 30:
            target.set_status('POISONED')
            print(f'{target.get_name()} is now poisoned!')


class StoneEdge(PhysicalMove):

    def __init__(self):
        super().__init__()
        self.base_pwr = 100
        self.accuracy = 85
        self.name = 'Stone Edge'
        self.type = 'ROCK'

class Surf(SpecialMove):

    def __init__(self):
        super().__init__()
        self.base_pwr = 90
        self.name = 'Surf'
        self.type = 'WATER'


class WildCharge(PhysicalMove):

    def __init__(self):
        super().__init__()
        self.base_pwr = 90
        self.name = 'Wild Charge'
        self.type = 'ELECTRIC'

    def self_effect(self, target):
        target.lose_hp(target.get_max_hp() / 16)
        print(f'{target.get_name()} took recoil damage!')


print('Moves loaded!')
