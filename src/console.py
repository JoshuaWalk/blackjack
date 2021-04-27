'''
name:
    console.py
description:
    console display for blackjack
'''
import os, sys
from actions import Actions

class Console():
    '''
    description: 
        console controll for the blackjack game.
        this module controls the display of the application
    '''
    def __init__(self):
        self.game = Actions()
        self.menu = {
            "0" : self.add_player,
            "1" : self.display_players,
            "2" : self.start_game,
            "q" : self.quit
        }
        self.choices = {
            "1" : self.hit,
            "2" : None,
            "q" : self.quit
        }

    def run_menu(self):
        ''' start menu for game '''
        self.display_title()
        self.print_menu()
        while True:

            choice = input('Enter Option:\n')

            action = self.menu.get(choice)
            if action:
                action()
            else:
                print('invalid option')

    def add_player(self):
        name = input('What is your name?\n')
        self.game.add_player(name)

    def start_game(self):
        self.game.deal()
        for player in self.game.players:
            self.player_turn(player)

    def player_turn(self, player):
        self.print_options()
        while True:
            choice = input('What would you like to do?')
            action = self.choices.get(choice)
            if choice == 2:
                break
            elif action:
                action(player)
            else: 
                print('invalid option')

    def hit(self, player):
        self.game.hit(player)
        self.display_player(player)

    
    def player_busts(self, player):
        print(f'{player.name} busts!')

    def display_winner(self):
        winner = self.game.winner
        print('=========== GAME OVER ==============')
        print(f'======= {winner.name} wins! =======')
        print(f'Total: {winner.total}')

    def quit(self):
        ''' terminates program '''

        print('Thanks for playing!!')
        sys.exit(0)


# DISPLAY FUNCTIONS 

    def display_title(self):
        os.system('clear')
        print('\n==================================')
        print(f'=========== {self.game.name} ============')
        print('==================================')

    def print_menu(self):
        print('[0] Add Player')
        print('[1] List Players')
        print('[2] Start Game')
        print('[q] Quit')    

    def print_options(self):
        print('\nOPTIONS: ')
        print('[1] - Hit')
        print('[2] - Stand')
        print('[q] - Quit')    

    def display_card(self, card):
        ''' displays a card '''
        print(f'{card.value} of {card.suit}')

    def display_hand(self, player):
        ''' displays a players hand '''
        for card in player.hand:
            self.display_card(card)

    def display_player(self, player):
        ''' displays info for single player '''
        print(player.name, f'total: {player.total}\nPlayers Hand:')
        self.display_hand(player)

    def display_players(self):
        ''' displays all player names '''
        for player in self.game.players:
            print(player.name)