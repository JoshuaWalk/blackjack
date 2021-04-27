import pytest
from src.card import Deck
from src.game import Game
from src.console import Console
from tests.params import low_cards

@pytest.fixture
def empty_deck():
    deck = Deck()
    return deck

@pytest.fixture
def full_deck():
    deck = Deck()
    deck.build()
    return deck

@pytest.fixture
def game():
    game = Game()
    return game

@pytest.fixture
def console():
    console = Console(game)
    return console

@pytest.mark.card
@pytest.mark.parametrize("card, out", low_cards)
def test_show(card, out, console):
    assert console.display_card(card) == out


@pytest.mark.deck
def test_deck_length(first_deck):
    assert len(first_deck.cards) == 52


