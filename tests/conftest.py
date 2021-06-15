import pytest

@pytest.fixture
def empty_deck():
    deck = Deck()
    return deck

@pytest.fixture
def first_deck():
    deck = Deck()
    deck.build()
    return deck