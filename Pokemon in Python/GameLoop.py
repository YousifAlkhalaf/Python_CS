import Moves
import Pokemon

def all_pokemon_fainted(player):
    for pokemon in player:
        if pokemon.get_status() != 'FAINTED':
            return False
    return True

def select_pokemon(player):
    out_str = ''
    for i in range(len(player)):
        out_str = f"{i + 1}.\t{player[i].__str__()}\n"
        print(out_str)
    
    num = -1
    while num not in range (1, len(player)):
        num = int(input('Enter a number: '))
        if num > len(player) or num < 1:
            print('Invalid input. Try again.')
        elif player[num-1].get_status() == 'FAINTED':
            print(f'{player[num].get_name()} cannot fight!')
            num = -1
        else:
            return num-1

def game_loop(p1, num1, p2, num2):
    pkmn1 = p1[num1]
    pkmn2 = p2[num2]
    print(pkmn1.get_name() + ' VS ' + pkmn2.get_name())
    return 5

player1 = []
player1.append(Pokemon.Starmie([Moves.Surf(), Moves.Psychic(), Moves.Recover(), Moves.ConfuseRay()]))
player1.append(Pokemon.Venusaur([Moves.EnergyBall(), Moves.SludgeBomb(), Moves.Rest(), Moves.PoisonPowder()]))
player2 = []
player2.append(Pokemon.Jynx([Moves.IceBeam(), Moves.Psychic(), Moves.ShadowBall(), Moves.LovelyKiss()]))

print('Player 1, select your Pokemon\n')
p1_pkmn_num = select_pokemon(player1)
print('Player 2, select your Pokemon\n')
p2_pkmn_num = select_pokemon(player2)

while not all_pokemon_fainted(player1) and not all_pokemon_fainted(player2):
    game_loop(player1, p1_pkmn_num, player2, p2_pkmn_num)
    
