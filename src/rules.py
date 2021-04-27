''' 
name:
    rules.py
description: 
    implements game logic
'''

from player import BlackjackDealer
from game import Game

class Rules(Game):
    def __init__(self):
        Game.__init__(self)
        self.name = 'Blackjack'
        self.dealer = BlackjackDealer()
        self.winner = self.dealer

    def bust_check(self, player):
        self.busted_aces(player)
        if player.total > 21:
            player.is_busted = True

    def busted_aces(self, player):
        for card in player.hand:
            if card.value == 'Ace' and card.is_used == False:
                if player.total <= 21: break
                player.total -= 10
                card.is_used = True

