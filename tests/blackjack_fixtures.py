import pytest
from src.card import Card
from src.blackjack_rules import Blackjack

@pytest.fixture
def blackjack():
    game = Blackjack()
    return game

@pytest.fixture
def blackjack_1p(blackjack):
    blackjack.add_player('Josh')
    return blackjack

@pytest.fixture
def blackjack_2p(blackjack_1p):
    blackjack_1p.add_player('Kev')
    return blackjack_1p

@pytest.fixture
def blackjack_5p(blackjack_2p):
    blackjack_2p.add_player('Rich')
    blackjack_2p.add_player('Gerald')
    blackjack_2p.add_player('Harold')
    return blackjack_2p

@pytest.fixture
def adding_to_total(blackjack_1p):
    game = blackjack_1p
    game.card_to_hand(game.players[0], Card('Spades', 5))
    return game

@pytest.fixture
def adding_to_ace(blackjack_1p):
    game = blackjack_1p
    game.card_to_hand(game.players[0], Card('Spades', 'Ace'))
    game.card_to_hand(game.players[0], Card('Spades', 7))
    return game

@pytest.fixture
def two_high_cards(blackjack_1p):
    game = blackjack_1p
    game.card_to_hand(game.players[0], Card('Diamonds', 'King'))
    game.card_to_hand(game.players[0], Card('Spades', 8))
    return game

@pytest.fixture
def game_with_3p():
    game = Blackjack()
    game.add_player('Fry')
    game.add_player('Leela')
    game.add_player('Bender')
    return game

@pytest.fixture
def dealt_game_3p(game_with_3p):
    game = game_with_3p
    game.card_to_hand(game.players[0], Card('Spades', 10))
    game.card_to_hand(game.players[0], Card('Diamonds', 5))
    game.card_to_hand(game.players[1], Card('Diamonds', 'King'))
    game.card_to_hand(game.players[1], Card('Hearts', 5))
    game.card_to_hand(game.players[2], Card('Clubs', 7))
    game.card_to_hand(game.players[2], Card('Spades', 8))
    game.card_to_hand(game.dealer, Card('Hearts', 9))
    game.card_to_hand(game.dealer, Card('Clubs', 6))
    return game

@pytest.fixture
def dealer_wins(dealt_game_3p):
    game = dealt_game_3p
    game.card_to_hand(game.dealer, Card('Diamonds', 3))
    return game

@pytest.fixture
def dealer_busts(dealt_game_3p):
    game = dealt_game_3p
    game.card_to_hand(game.players[0], Card('Diamonds', 4))
    game.card_to_hand(game.players[1], Card('Diamonds', 8))
    game.card_to_hand(game.players[2], Card('Diamonds', 5))
    game.card_to_hand(game.dealer, Card('Diamonds', 'Jack'))
    return game

@pytest.fixture
def some_win(dealt_game_3p):
    game = dealt_game_3p
    game.card_to_hand(game.players[0], Card('Diamonds', 5))
    game.card_to_hand(game.players[1], Card('Clubs', 6))
    game.card_to_hand(game.players[2], Card('Diamonds', 2))
    game.card_to_hand(game.dealer, Card('Hearts', 3))
    return game

@pytest.fixture
def all_players_win(dealt_game_3p):
    game = dealt_game_3p
    game.card_to_hand(game.players[0], Card('Spades', 4))
    game.card_to_hand(game.players[1], Card('Hearts', 5))
    game.card_to_hand(game.players[2], Card('Clubs', 3))
    game.card_to_hand(game.dealer, Card('Diamonds', 2))
    return game