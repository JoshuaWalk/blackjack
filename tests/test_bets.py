import pytest
from game_params import *
from blackjack_fixtures import *

@pytest.mark.bet
def test_bet_dealer_busts(dealer_busts):
    game = dealer_busts
    players = dealer_busts.players
    game.evaluate_payout_all()
    errors = []
    print(players[0].reward, 'HEEEERRREEEEE')
    if not players[0].reward == 1000000:
        errors.append('Fry')
    if not players[1].reward == 0:
        errors.append('Leela')
    if not players[2].reward == 160:
        errors.append('Bender')
    assert not errors

@pytest.mark.bet
def test_bet_dealer_wins(dealer_wins):
    game = dealer_wins
    players = dealer_wins.players
    game.evaluate_payout_all()
    errors = []
    if not players[0].reward == 0:
        errors.append('Fry')
    if not players[1].reward == 0:
        errors.append('Leela')
    if not players[2].reward == 0:
        errors.append('Bender')
    assert not errors

@pytest.mark.bet
def test_bet_some_win(some_win):
    game = some_win
    players = some_win.players
    game.evaluate_payout_all()
    errors = []
    if not players[0].reward == 1000000:
        errors.append('Fry')
    if not players[1].reward == 600:
        errors.append('Leela')
    if not players[2].reward == 0:
        errors.append('Bender')
    assert not errors

@pytest.mark.bet
def test_bet_all_win(all_players_win):
    game = all_players_win
    players = all_players_win.players
    game.evaluate_payout_all()
    errors = []
    if not players[0].reward == 1000000:
        errors.append('Fry')
    if not players[1].reward == 600:
        errors.append('Leela')
    if not players[2].reward == 160:
        errors.append('Bender')
    assert not errors