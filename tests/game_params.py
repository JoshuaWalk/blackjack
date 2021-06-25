from src.card import Card


low_cards = [
    ('Spades', 3, '3 of Spades'),
    ('Diamonds', 4, '4 of Diamonds'),
    ('Diamonds', 7, '7 of Diamonds'),
    ('Hearts', 2, '2 of Hearts'),
    ('Spades', 'Ace', 'Ace of Spades'),
    ('Clubs', 3, '3 of Clubs')
]

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

bust_check =[
    (Card('Spades', 3), False),
    (Card('Diamonds', 4), True),
    (Card('Diamonds', 7), True),
    (Card('Hearts', 2), False),
    (Card('Spades', 'Ace'), False),
]

player_list = [
    ('Josh', 50, 'Josh'),
    ('Ethan', 74, 'Ethan'),
    ('Kirsten', 53, 'Kirsten'),
    ('AJ', 51, 'AJ')
]

better_list = [(item, item) for item in player_list]
