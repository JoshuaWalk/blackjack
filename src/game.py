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
        deck.build()
        deck.shuffle()

    def add_player(self, player):
        self.players.append(Player(player))
