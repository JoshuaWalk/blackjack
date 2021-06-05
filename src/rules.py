''' 
name:
    rules.py
description: 
    implements game logic
'''

from player import BlackjackDealer
from game import Game

class Table():
    def __init__(self):
        Game.__init__(self)
        self.name = 'Blackjack'
        self.dealer = BlackjackDealer()
        self.winner = []



    

