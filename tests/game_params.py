from src.card import Card

card_and_value =[
    (Card('Spades', 3), 3),
    (Card('Diamonds', 4), 4),
    (Card('Diamonds', 7), 7),
    (Card('Hearts', 2), 2),
    (Card('Spades', 'Ace'), 11),
    (Card('Clubs', 3), 3)
]

player_list = [
    'Josh',
    'Ethan',
    'Kirsten',
    'AJ'
]

better_list = [(item, item) for item in player_list]
