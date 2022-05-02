import Moves
import Pokemon

def allPokemonFainted(player):
    for pokemon in player:
        if pokemon.get_status() != 'FAINTED':
            return False
    return True

def selectPokemon(player):
    out_str = ''
    for i in range(len(player)):
        out_str = f"{i + 1}.\t{player[i].__str__()}\n"
        print(out_str)
    
    num = -1
    while num not in range (1, len(player)):
        num = int(input('Enter a number: '))
        if player[num].get_status() == 'FAINTED':
            print(f'{player[num].get_name()} cannot fight!')
            num = -1
        

player1 = []
player1.append(Pokemon.Starmie([Moves.Surf(), Moves.Psychic(), Moves.Recover(), Moves.ConfuseRay()]))
player1.append(Pokemon.Venusaur([Moves.EnergyBall(), Moves.SludgeBomb(), Moves.Rest(), Moves.PoisonPowder()]))
player2 = []
player2.append(Pokemon.Jynx([Moves.IceBeam(), Moves.Psychic(), Moves.ShadowBall(), Moves.LovelyKiss()]))


print('Player 1, select your Pokemon\n')
print(selectPokemon(player1))

while not allPokemonFainted(player1) and not allPokemonFainted(player2):
    break
