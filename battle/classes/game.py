import random
from .magic import Spell

#color in terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, hp, mp, attack, defense, magic):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.attack_low = attack - 10
        self.attack_hight = attack + 10
        self.defense = defense
        self.magic = magic
        self.action = ['Attack', 'Magic']

    def generate_damage(self):
        return random.randrange(self.attack_low, self.attack_hight)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
        return self.hp

    def heal(self, heal_point):
        self.hp += heal_point
    
    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp
    
    def reduce_mp(self, cost):
        if self.mp >= cost:
            self.mp -= cost
    
    def choose_action(self):
        index = 1
        print('Actions:')
        for item in self.action:
            print(str(index) + ':', item)
            index += 1
    
    def choose_magic(self):
        index = 1
        print('Magic:')
        for spell in self.magic:
            print(str(index) + ':', spell.name, '(cost:', spell.cost, ')')
            index += 1