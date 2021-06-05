''' 
name:
    game.py
description:
    handles players and deck
'''
from card import Deck
from player import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []
    
    def init_deck(self):
        deck = self.deck 
        deck.multi_decks(5)
        deck.multi_shuffle(5)

    def add_player(self, player):
        self.players.append(Player(player))

    
