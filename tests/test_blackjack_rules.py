import pytest
from game_params import *
from blackjack_fixtures import *

@pytest.mark.dealing
def test_deal_1(blackjack_1p):
    blackjack_1p.deal()
    for player in blackjack_1p.players:
        assert len(player.hand) == 2

@pytest.mark.dealing
def test_deal_2(blackjack_2p):
    blackjack_2p.deal()
    for player in blackjack_2p.players:
        assert len(player.hand) == 2

@pytest.mark.dealing
def test_deal_5(blackjack_5p):
    blackjack_5p.deal()
    for player in blackjack_5p.players:
        assert len(player.hand) == 2

@pytest.mark.dealing
def test_deal_dealer(blackjack_2p):
    blackjack_2p.deal()
    assert len(blackjack_2p.dealer.hand) == 2

@pytest.mark.game
def test_player_list_5(blackjack_5p):
    assert len(blackjack_5p.players) == 5

@pytest.mark.hitting
@pytest.mark.parametrize("card, value", card_and_value)
def test_hitting(card, value, blackjack_1p):
    game = blackjack_1p
    game.card_to_hand(game.players[0], card)
    assert game.players[0].total == value

@pytest.mark.hitting
@pytest.mark.parametrize("card, value", card_to_total)
def test_hitting_2(card, value, adding_to_total):
    game = adding_to_total
    game.card_to_hand(game.players[0], card)
    assert game.players[0].total == value

@pytest.mark.hitting
@pytest.mark.parametrize("card, value", card_to_ace)
def test_hitting_3(card, value, adding_to_ace):
    game = adding_to_ace
    game.card_to_hand(game.players[0], card)
    assert game.players[0].total == value

@pytest.mark.hitting
@pytest.mark.parametrize('card, value', bust_check)
def test_busting(card, value, two_high_cards):
    game = two_high_cards
    game.card_to_hand(game.players[0], card)
    assert game.players[0].is_busted == value

@pytest.mark.winning
def test_some_win(some_win):
    some_win.win_check()
    assert len(some_win.winner) == 2
    
@pytest.mark.winning
def test_some_win_names(some_win):
    some_win.win_check()
    assert some_win.winner[0].name == 'Fry' and some_win.winner[1].name == 'Leela'

@pytest.mark.winning
def test_all_players_win(all_players_win):
    all_players_win.win_check()
    assert len(all_players_win.winner) == 3

@pytest.mark.winning
def test_dealer_busts(dealer_busts):
    dealer_busts.win_check()
    assert len(dealer_busts.winner) == 2

@pytest.mark.winning
def test_dealer_wins(dealer_wins):
    dealer_wins.win_check()
    assert len(dealer_wins.winner) == 0