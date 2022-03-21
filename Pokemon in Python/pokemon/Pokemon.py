import math

class Pokemon(object):

    def __init__(self):
        pass

    def calc_hp(self, base_stat, level):
        hp = ((2 * base_stat) * level)/100 + level + 10
        return math.ceil(hp)

    def calc_stat(self, base_stat, level):
        stat = ((2 * base_stat) * level)/100 + 5
        return math.ceil(stat)
