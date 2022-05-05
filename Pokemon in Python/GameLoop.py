import Moves
import Pokemon

class Player(object):
    
    def __init__(self, p_num, party):
        self.p_num = p_num
        self.party = party
        self.pkmn_num = -1
        self.move_num = -1
    
    def __str__(self):
        return 'Player ' + self.p_num
    
    def get_party(self):
        return self.party
    
    def get_out_pokemon(self):
        return self.party[self.pkmn_num]
    
    def get_move_num(self):
        return self.move_num
    
    def all_pokemon_fainted(self):
        for pokemon in self.party:
            if pokemon.get_status() != 'FAINTED':
                return False
        return True
    
    def select_pokemon(self):
        
        party = self.party
        out_str = ''
        for i in range(len(party)):
            out_str = f"{i + 1}.\t{party[i].__str__()}\n"
            print(out_str)
        
        num = -1
        while num not in range (1, len(party)):
            num = int(input('Enter a number: '))
            print(num)
            if num > len(party) or num < 1:
                print('Invalid input. Try again.')
            elif party[num-1].get_status() == 'FAINTED':
                print(f'{party[num].get_name()} cannot fight!')
                num = -1
            else:
                self.pkmn_num = num-1
                return
    
    def select_move(self):
        pokemon = self.party[self.pkmn_num]
        if not pokemon.sleep() and not pokemon.paralysis():
            moves = pokemon.get_moves()
            for i in range(len(moves)):
                print(f'{i + 1}.\t{moves[i].__str__()}')
        
        num = -1
        while num not in range (1, len(moves)):
            num = int(input('Enter a number: '))
            if num > len(moves) or num < 1:
                print('Invalid input. Try again.')
            else:
                self.move_num = num - 1

def main_menu(player):
    print('1.\tFIGHT')
    print('2.\tPOKEMON')
    
    num = -1
    while num not in range (1, 3):
        num = input('Enter a number: ')
        if num == 1:
            player.select_move()
        elif num == 2:
            player.select_pokemon()
        else:
            print('Invalid input. Try again.')            

def game_loop(player1, player2):
    pkmn1 = player1.get_out_pokemon()
    pkmn2 = player2.get_out_pokemon()
    print(pkmn1.get_name() + ' VS ' + pkmn2.get_name())
    
    print('Player 1\'s turn!')
    main_menu(player1, p1_pkmn_num)
    print('Player 2\'s turn!')
    main_menu(player2, p2_pkmn_num)
    
    if pkmn1.faster_than(pkmn2):
        move_run(player1, player2)

def move_run(attacker, defender):
    attacking_pkmn = attacker.get_out_pokemon()
    defending_pkmn = defender.get_out.pokemon()
    move = attacking_pkmn.get_moves()[attacker.move_num]
    
    if move.accuracy_check():
        pass
    else:
        print(f'{attacking_pkmn.get_name()} missed!')
    
    
        
p1_pkmn_num = 0
p2_pkmn_num = 0

party1 = []
party1.append(Pokemon.Starmie([Moves.Surf(), Moves.Psychic(), Moves.Recover(), Moves.ConfuseRay()]))
party1.append(Pokemon.Venusaur([Moves.EnergyBall(), Moves.SludgeBomb(), Moves.Rest(), Moves.PoisonPowder()]))
player1 = Player(1, party1)
party2 = []
party2.append(Pokemon.Jynx([Moves.IceBeam(), Moves.Psychic(), Moves.ShadowBall(), Moves.LovelyKiss()]))
player2 = Player(2, party2)

print('Player 1, select your Pokemon\n')
player1.select_pokemon()
print('Player 2, select your Pokemon\n')
player2.select_pokemon()

while not player1.all_pokemon_fainted() and not player2.all_pokemon_fainted():
    game_loop(player1, player2)
    
