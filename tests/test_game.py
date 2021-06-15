import pytest
from src.game import Game, Player
from tests.game_params import better_list

@pytest.fixture
def game():
    game = Game()
    return game

@pytest.fixture
def add_player_to_game(game, player):
    game.add_player(player)
    return game


@pytest.mark.game
@pytest.mark.parametrize("player, out", better_list)
def test_add_player(player, out, game):
    game.add_player(player)
    assert game.players[0].name == out