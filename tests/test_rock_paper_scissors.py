from main import RockPaperScissorsSimulator


def test_game_print_options():
    game = RockPaperScissorsSimulator()
    assert game.print_options()


