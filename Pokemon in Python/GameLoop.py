import Moves
import Pokemon


class Player(object):

    def __init__(self, party, p_num):
        self.party = party
        self.p_num = p_num
        self.prev_pkmn_num = -1
        self.pkmn_num = -1
        self.move_num = -1

    def __str__(self):
        return 'Player ' + str(self.p_num)

    def has_switched(self):
        return self.prev_pkmn_num != self.pkmn_num

    def update(self):
        self.prev_pkmn_num = self.pkmn_num

    def get_party(self):
        return self.party

    def get_out_pokemon(self):  # Pokemon currently in play
        return self.party[self.pkmn_num]

    def get_move_num(self):
        return self.move_num

    def set_move_num(self, num):
        self.move_num = -1

    def pkmn_fainted(self):
        if self.party[self.pkmn_num].has_fainted() and not self.all_pokemon_fainted():
            self.select_pokemon(False)

    def all_pokemon_fainted(self):
        for pokemon in self.party:
            if pokemon.get_status() != 'FAINTED':
                return False
        return True

    # Player selects from Pokemon in party, can only select non-fainted Pokemon
    # If the Pokemon selected is already out, or if the switch penalty is turned off,
    # the Pokemon can act in the same turn. Otherwise, it can't act until the next turn.
    def select_pokemon(self, switch_penalty=True):

        print(f'{self.__str__()}, select your Pokemon!\n')
        party = self.party
        for i in range(len(party)):
            out_str = f"{i + 1}. {party[i].__str__()}\n"
            print(out_str + '\n')

        menu_num = -1
        while menu_num not in range(1, len(party)):
            menu_num = enter_number()
            if menu_num > len(party) or menu_num < 1:
                print('Invalid input. Try again.')
            elif party[menu_num-1].get_status() == 'FAINTED':
                print(
                    f'{party[menu_num-1].get_name()} has fainted and cannot fight!')
                menu_num = -1
            else:
                self.pkmn_num = menu_num-1
                if not switch_penalty:
                    self.prev_pkmn_num = self.pkmn_num
                return

    # Select 1 of up to 4 moves of Pokemon currently in play.
    def select_move(self):

        print(f'{self.__str__()}, select a move!')
        self.move_num = -1
        pokemon = self.party[self.pkmn_num]

        print()
        moves = pokemon.get_moves()
        if not pokemon.is_immobilized():
            for i in range(len(moves)):
                print(f'{i + 1}.\t{moves[i].__str__()}\n')
        else:
            return

        menu_num = -1
        while menu_num < 1 or menu_num > len(moves):
            menu_num = enter_number()
            if menu_num > len(moves) or menu_num < 1:
                print('Invalid input. Try again.')
            else:
                self.move_num = menu_num - 1

    def main_menu(self):
        print(f'\n{self.__str__()}\'s turn!')
        print('1.\tFIGHT')
        print('2.\tPOKEMON')

        menu_num = -1
        while menu_num < 1 or menu_num > 2:
            menu_num = enter_number()
            if menu_num == 1:
                self.select_move()
            elif menu_num == 2:
                self.select_pokemon()
                if not self.has_switched():
                    self.select_move()
            else:
                print('Invalid input. Try again.')


def enter_number():
    try:
        menu_num = int(input('Enter a number: '))
    except ValueError:
        menu_num = -1
    return menu_num


def move_run(attacker, defender):  # Routine for attacker using a move on defender
    attacking_pkmn = attacker.get_out_pokemon()
    defending_pkmn = defender.get_out_pokemon()
    attacking_pkmn.run_stun_statuses()

    if not attacking_pkmn.is_immobilized() and not attacker.has_switched():
        move = attacking_pkmn.get_moves()[attacker.get_move_num()]
        multiplier = defending_pkmn.calc_type_effectiveness(move.get_type())
        print(f'{attacking_pkmn.get_name()} uses {move.get_name()}!')

        if multiplier == 0:
            print('It had no effect!')
        elif not isinstance(move, Moves.StatusMove):
            if multiplier > 1:
                print('It\'s super effective!')
            elif multiplier < 1:
                print('It\'s not very effective.')

        if move.accuracy_check():
            damage = move.calc_damage(
                attacking_pkmn, defending_pkmn, multiplier)
            defending_pkmn.lose_hp(damage)

            if multiplier != 0:
                move.self_effect(attacking_pkmn)
                move.foe_effect(defending_pkmn)
        else:
            print(f'{attacking_pkmn.get_name()} missed!')
    attacker.set_move_num(-1)


# Loop for running the game
def game_loop(player1, player2):
    pkmn1 = player1.get_out_pokemon()
    pkmn2 = player2.get_out_pokemon()

    display_str = pkmn1.get_name() + ' VS ' + pkmn2.get_name()
    display_str += '\n\n' + pkmn1.__str__()
    display_str += '\n' + pkmn2.__str__()
    print(display_str)

    player1.main_menu()
    player2.main_menu()

    # Moves execute in order based on Pokemon speed
    if pkmn1.faster_than(pkmn2):
        move_run(player1, player2)
        player2.pkmn_fainted()
        move_run(player2, player1)
        player1.pkmn_fainted()
    else:
        move_run(player2, player1)
        player1.pkmn_fainted()
        move_run(player1, player2)
        player2.pkmn_fainted()

    # Poison condition runs
    pkmn1.poison()
    pkmn2.poison()

    player1.pkmn_fainted()
    player2.pkmn_fainted()

    # Updates players so switch penalties are no longer in effect
    player1.update()
    player2.update()


def win_conditions(player1, player2):  # Who wins
    if player1.all_pokemon_fainted():
        print('Player 2 wins!')
    else:
        print('Player 1 wins!')


party1 = []
party1.append(Pokemon.Starmie(
    [Moves.Surf(), Moves.Psychic(), Moves.Recover(), Moves.ConfuseRay()]))
party1.append(Pokemon.Venusaur(
    [Moves.EnergyBall(), Moves.SludgeBomb(), Moves.Rest(), Moves.PoisonPowder()]))
player1 = Player(party1, 1)

party2 = []
party2.append(Pokemon.Jynx(
    [Moves.IceBeam(), Moves.Psychic(), Moves.ShadowBall(), Moves.LovelyKiss()]))
player2 = Player(party2, 2)

player1.select_pokemon(False)
player2.select_pokemon(False)

while not player1.all_pokemon_fainted() and not player2.all_pokemon_fainted():
    game_loop(player1, player2)
win_conditions(player1, player2)
