from src.card import Card

card_and_value =[
    (Card('Spades', 3), 3),
    (Card('Diamonds', 4), 4),
    (Card('Diamonds', 7), 7),
    (Card('Hearts', 2), 2),
    (Card('Spades', 'Ace'), 11),
    (Card('Clubs', 3), 3)
]

card_to_total =[
    (Card('Spades', 3), 8),
    (Card('Diamonds', 4), 9),
    (Card('Diamonds', 7), 12),
    (Card('Hearts', 2), 7),
    (Card('Spades', 'Ace'), 16),
]

card_to_ace =[
    (Card('Spades', 3), 21),
    (Card('Diamonds', 4), 12),
    (Card('Diamonds', 7), 15),
    (Card('Hearts', 2), 20),
    (Card('Spades', 'Ace'), 19),
]

player_list = [
    'Josh',
    'Ethan',
    'Kirsten',
    'AJ'
]

better_list = [(item, item) for item in player_list]
