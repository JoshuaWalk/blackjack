''' 
name:
    game.py
description:
    handles players and deck
'''
from src.card import Deck
from src.player import Player


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

    def show(self):
        for player in self.players:
            return player.name
