'''
name:
    actions.py
description:
    deals cards between decks and players, child of game and rules
'''

from rules import *

class Actions(Rules):
    def __init__(self):
        Rules.__init__(self)
        self.init_deck()

    def deal(self):
        ''' deals 2 cards to every player in the game '''
        for player in self.players:
            self.hit(player)
            self.hit(player)
        self.hit(self.dealer)
        self.hit(self.dealer)

    def hit(self, player):
        ''' takes card from deck to player hand '''
        card = self.deck.cards.pop()
        player.hand.append(card)
        self.add_card(card, player)

    def add_card(self, card, player):
        ''' adds value of card to players total '''
        if card.value == 'Ace' and player.total + 11 > 21:
            player.total += 1
            card.is_used = True
        elif card.value == 'Ace' and player.total + 11 <= 21:
            player.total += 11
        elif card.value == 'Jack' or card.value == 'Queen' or card.value == 'King':
            player.total += 10
        else: player.total += card.value

    def dealer_turn(self):
        ''' if dealer has less than 17 points, dealer hits'''
        if self.dealer.total < 17 and self.dealer.total < self.winner.total:
            self.hit(self.dealer)
            self.dealer_play()

    def dealer_play(self):
        ''' if there are active players, dealer takes a turn '''
        for player in self.player_list:
            if player.is_busted == False:
                self.dealer_turn()

    def determine_winner(self):
        ''' sets the winner of the game '''
        for player in self.players:
            if player.total > self.winner.total and player.total <= 21:
                self.winner = player
