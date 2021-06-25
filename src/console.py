'''
name:
    console.py
description:
    console display for blackjack
'''
import os, sys
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
        wager = input('How much do you want to bet?\n')
        self.game.add_player(name, wager)

    def start_game(self):
        self.game.deal()
        for player in self.game.players:
            self.player_turn(player)
        self.dealer_turn()
        self.display_payout()
        self.restart()
        
    def player_turn(self, player):
        try:
            while player.total <= 21:
                self.display_players()
                self.display_hand(player)
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
        self.display_hand(dealer)
        while dealer.total < 17:
            self.hit(dealer)
            self.display_hand(dealer)
            
    def hit(self, player):
        self.game.hit(player)

    def restart(self):
        self.game.reset()
        self.reset_bets()
        self.start_game()

    def reset_bets(self):
        for player in self.game.players:
            new_bet = input(f'{player.name}:\n What would you like to bet?\n')
            self.game.reset_wager(player, new_bet)

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

    def player_busts(self, player):
        if player.total > 21:
            print(f'{player.name} busts!')

    def bust_announcements(self):
        for player in self.game.players:
            self.player_busts(player)

    def display_payout(self):
        for player in self.game.players:
            self.game.evaluate_payout(player)
            self.determine_payout(player)
    
    def determine_payout(self, player):
            if player.reward == 0:
                print(f'{player.name} lost bet')
            elif player.reward == player.wager:
                print(f'{player.name} tied with dealer, bet is returned {player.reward}')
            else: print(f'{player.name} won! they recieved {player.reward}')

    def display_winner(self):
        if self.game.winner == []:
            print('DEALER WINS ALL')
        for winner in self.game.winner:
            print('=========== GAME OVER ==============')
            print(f'======= {winner.name} wins! =======')
            print(f'Total: {winner.total}')


class PlayerStood(Exception): pass