''' 
name: 
    card.py

description:
    card and deck objects for blackjack
'''

import random

class Card:
    '''
    description:
        a single card of a game deck
    attributes:
        suit (str) - suit of card
        value (str/num) - value of card
        is_used (bool) - for aces (1 or 11 points)
    '''
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.is_used = False

    def show(self):
        return (f'{self.value} of {self.suit}')

class Deck:
    '''
    description:
        standard game deck, 52 cards 
        Ace to King
        Spades, Diamonds, Clubs, Hearts

    attributes:
        cards (list of card objects)

    methods:
        build - creates a standard 52 card deck
        shuffle - arranges the cards in random order
        clear - removes all cards from deck
        draw - returns a card in an array
        show - prints every card in deck
    '''
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def build(self):
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        for s in suits:
            for v in values:
                self.add_card(Card(s, v))

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        print('shuffling cards\n')
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, len(self.cards)-1)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
