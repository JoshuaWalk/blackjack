import pytest
from src.blackjack_rules import Blackjack
from tests.game_params import *

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
def deal_to_players(game):
    game.deal()
    return game

@pytest.mark.blackjack
def test_deal_1(blackjack_1p):
    blackjack_1p.deal()
    for player in blackjack_1p.players:
        assert len(player.hand)== 2

@pytest.mark.blackjack
def test_deal_2(blackjack_2p):
    blackjack_2p.deal()
    for player in blackjack_2p.players:
        assert len(player.hand)== 2

@pytest.mark.blackjack
def test_deal_5(blackjack_5p):
    blackjack_5p.deal()
    for player in blackjack_5p.players:
        assert len(player.hand)== 2

@pytest.mark.blackjack
def test_deal_dealer(blackjack_2p):
    blackjack_2p.deal()
    assert len(blackjack_2p.dealer.hand) == 2

@pytest.mark.blackjack
def test_player_list_5(blackjack_5p):
    assert len(blackjack_5p.players) == 5


@pytest.mark.blackjack
@pytest.mark.parametrize("card, value", card_and_value)
def test_hitting(card, value, blackjack_1p):
    game = blackjack_1p
    game.card_to_hand(game.players[0], card)
    assert game.players[0].total == value