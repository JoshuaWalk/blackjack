import pytest
from src.game import *
from tests.game_params import *

@pytest.fixture
def game():
    game = Game()
    return game

@pytest.fixture
def add_player_to_game(game, player):
    new = Player(player)
    game.add_player(new)
    return game


@pytest.mark.game
@pytest.mark.parametrize("player, out", better_list)
def test_add_player(player, out, game):
    game.add_player(player)
    assert game.show() == out