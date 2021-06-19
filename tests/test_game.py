import pytest
from src.game import Game
from game_params import player_list

@pytest.fixture
def game():
    game = Game()
    return game

@pytest.fixture
def add_player_to_game(game, player):
    game.add_player(player)
    return game


@pytest.mark.game
@pytest.mark.parametrize("name, bet, out", player_list)
def test_add_player(name, bet, out, game):
    game.add_player(name, bet)
    assert game.players[0].name == out