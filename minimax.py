from game import Game, print_board
from random import choice

INFINITY = float("inf")
NEGATIVE_INFINITY = float("-inf")
game = Game()


def max_value(game: Game, board, alpha=NEGATIVE_INFINITY, beta=INFINITY):
    # doing it this way lets you calculate utility and if Terminal state with one call
    game_over = game.is_game_over(board)
    if game_over in [0, -1, 1]:
        return game_over

    v = NEGATIVE_INFINITY

    for move in game.moves(board):
        v = max(v, min_value(game, game.result(board, move), alpha, beta))
        if v >= beta:
            return v
        alpha = max(v, alpha)
    return v


def min_value(game: Game, board, alpha=NEGATIVE_INFINITY, beta=INFINITY):
    game_over = game.is_game_over(board)
    if game_over in [0, -1, 1]:
        return game_over

    v = INFINITY

    for move in game.moves(board):
        v = min(v, max_value(game, game.result(board, move), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v


def make_move(game: Game, player=1):
    current_board = game.current_board.copy()
    if player == -1:
        moves = {move: INFINITY for move in game.moves(current_board)}
        for move in moves.keys():
            moves[move] = max_value(game, game.result(current_board, move))
        lowest_value = min(moves.values())
        optimal_moves = [k for k, v in moves.items() if v == lowest_value]
        return choice(optimal_moves)

    moves = {move: NEGATIVE_INFINITY for move in game.moves(current_board)}
    for move in moves.keys():
        moves[move] = min_value(game, game.result(current_board, move))
    highest_value = max(moves.values())
    optimal_moves = [k for k, v in moves.items() if v == highest_value]
    return choice(optimal_moves)


def print_game_over_message_ai(winner):
    ai1_win_msg = r"""
    _    _    ___              __        ___
   / \  (_)  / _ \ _ __   ___  \ \      / (_)_ __  ___
  / _ \ | | | | | | '_ \ / _ \  \ \ /\ / /| | '_ \/ __|
 / ___ \| | | |_| | | | |  __/   \ V  V / | | | | \__ \
/_/   \_\_|  \___/|_| |_|\___|    \_/\_/  |_|_| |_|___/


    """
    ai2_win_msg = r"""
    _    _   _____                __        ___
   / \  (_) |_   _|_      _____   \ \      / (_)_ __  ___
  / _ \ | |   | | \ \ /\ / / _ \   \ \ /\ / /| | '_ \/ __|
 / ___ \| |   | |  \ V  V / (_) |   \ V  V / | | | | \__ \
/_/   \_\_|   |_|   \_/\_/ \___/     \_/\_/  |_|_| |_|___/

    """
    if winner == -1:
        print(ai2_win_msg)
    elif winner == 0:
        print("""
 ____
|  _ \\ _ __ __ ___      __
| | | | '__/ _` \\ \\ /\\ / /
| |_| | | | (_| |\\ V  V /
|____/|_|  \\__,_| \\_/\\_/

 """)
    elif winner == 1:
        print(ai1_win_msg)


def ai_v_ai():
    while True:
        print_board(game.current_board)
        print("\n")
        player = game.whos_turn(game.current_board)
        move = make_move(game, player)
        game.current_board[move] = player
        game_over = game.is_game_over(game.current_board)
        if game_over in [-1, 1, 0]:
            print_board(game.current_board)
            print("\n")
            print_game_over_message_ai(game_over)
            break


if __name__ == "__main__":
    ai_v_ai()
