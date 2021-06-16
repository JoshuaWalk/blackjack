'''
name:
    console.py
description:
    console display for blackjack
'''
import os, sys, time
from blackjack_rules import Blackjack

class Console():
    '''
    description: 
        console controll for the blackjack game.
        this module controls the display of the application
    '''
    def __init__(self):
        self.game = Blackjack()
        self.menu = {
            "0" : self.add_player,
            "1" : self.display_players,
            "2" : self.start_game,
            "q" : self.quit
        }
        
        self.choices = {
            "1" : self.hit,
            "2" : 'stand',
            "q" : self.quit
        }

    def run_menu(self):
        ''' start menu for game '''
        self.display_title()
        
        while True:
            self.print_menu()
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
            time.sleep(3)
        self.dealer_turn()
        self.end_game()
        self.restart()
        
    def player_turn(self, player):
        try:
            while player.total <= 21:
                self.display_players()
                self.display_hand(player)
                time.sleep(3)
                self.print_options(player)
                choice = input('What would you like to do?\n')
                action = self.choices.get(choice)
                if action:
                    if action == 'stand':
                        raise PlayerStood
                    elif action == 'q':
                        self.quit()
                    else: action(player)
                
        except PlayerStood: pass

    def dealer_turn(self):
        dealer = self.game.dealer
        while dealer.total < 17:
            self.hit(dealer)
            self.display_hand(dealer)
            time.sleep(3)

    def hit(self, player):
        self.game.hit(player)

    def end_game(self):
        self.game.win_check()
        self.bust_announcements()
        self.display_winner()

    def restart(self):
        self.game.reset()
        self.start_game()

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
        print('==================================')
        print('=========== MAIN MENU ============')
        print('==================================')
        print('[0] Add Player')
        print('[1] List Players')
        print('[2] Start Game')
        print('[q] Quit')  
        print('==================================')  

    def print_options(self, player):
        print('==================================')
        print(f"====== {player.name}'s OPTIONS =======")
        print('==================================')
        print('[1] - Hit')
        print('[2] - Stand')
        print('[q] - Quit')
        print('==================================')   

    def display_card(self, card):
        ''' displays a card '''
        print(f'{card.value} of {card.suit}')

    def display_hand(self, player):
        ''' displays a players hand '''
        print(f"========= {player.name}'s hand ========")
        print(f"========= TOTAL: {player.total} ===========")
        for card in player.hand:
            self.display_card(card)
        print('==================================')

    def display_players(self):
        ''' displays all player names '''
        print('============== DISPLAYING TABLE =================')
        if len(self.game.dealer.hand) == 2:
            self.game.dealer.show_one_card()
        else: self.display_hand(self.game.dealer)
        for player in self.game.players:
            self.display_hand(player) 
        print('================ END OF TABLE ===================')
        time.sleep(2)

    def player_busts(self, player):
        if player.total > 21:
            print(f'{player.name} busts!')

    def bust_announcements(self):
        for player in self.game.players:
            self.player_busts(player)

    def display_winner(self):
        if self.game.winner == []:
            print('DEALER WINS ALL')
        for winner in self.game.winner:
            print('=========== GAME OVER ==============')
            print(f'======= {winner.name} wins! =======')
            print(f'Total: {winner.total}')


class PlayerStood(Exception): pass