# Note: this is sloppy because the point was to learn minimax, and any time spent on not minimax would be waisted time  
from minimax import ai_v_ai, make_move
from game import Game, print_board


def print_game_over_message_pve(winner):
    ai_win_msg = r"""
    _    _  __        ___
   / \  (_) \ \      / (_)_ __  ___
  / _ \ | |  \ \ /\ / /| | '_ \/ __|
 / ___ \| |   \ V  V / | | | | \__ \
/_/   \_\_|    \_/\_/  |_|_| |_|___/

    """
    player_win_msg = r"""
__   __           __        ___
\ \ / /__  _   _  \ \      / (_)_ __
 \ V / _ \| | | |  \ \ /\ / /| | '_ \
  | | (_) | |_| |   \ V  V / | | | | |
  |_|\___/ \__,_|    \_/\_/  |_|_| |_|

    """
    if winner == 1:
        print(player_win_msg)
    elif winner == 0:
        print("""
 ____
|  _ \\ _ __ __ ___      __
| | | | '__/ _` \\ \\ /\\ / /
| |_| | | | (_| |\\ V  V /
|____/|_|  \\__,_| \\_/\\_/

 """)
    elif winner == -1:
        print(ai_win_msg)


def print_game_over_message_pvp(winner):
    player1_win_msg = r"""
 ____  _                          ___              __        ___
|  _ \| | __ _ _   _  ___ _ __   / _ \ _ __   ___  \ \      / (_)_ __  ___
| |_) | |/ _` | | | |/ _ \ '__| | | | | '_ \ / _ \  \ \ /\ / /| | '_ \/ __|
|  __/| | (_| | |_| |  __/ |    | |_| | | | |  __/   \ V  V / | | | | \__ \
|_|   |_|\__,_|\__, |\___|_|     \___/|_| |_|\___|    \_/\_/  |_|_| |_|___/
               |___/
    """
    player2_win_msg = r"""
 ____  _                         _____                __        ___
|  _ \| | __ _ _   _  ___ _ __  |_   _|_      _____   \ \      / (_)_ __  ___
| |_) | |/ _` | | | |/ _ \ '__|   | | \ \ /\ / / _ \   \ \ /\ / /| | '_ \/ __|
|  __/| | (_| | |_| |  __/ |      | |  \ V  V / (_) |   \ V  V / | | | | \__ \
|_|   |_|\__,_|\__, |\___|_|      |_|   \_/\_/ \___/     \_/\_/  |_|_| |_|___/
               |___/
    """
    if winner == 1:
        print(player1_win_msg)
    elif winner == 0:
        print("""
 ____
|  _ \\ _ __ __ ___      __
| | | | '__/ _` \\ \\ /\\ / /
| |_| | | | (_| |\\ V  V /
|____/|_|  \\__,_| \\_/\\_/

 """)
    elif winner == -1:
        print(player2_win_msg)


game = Game()


def p_v_ai():  # why make something so small be pretty. if it works it works. there is no future for the project; i have no features i want to make.
    while True:
        print_board(game.current_board)
        print("\n")
        player_move = retrieve_player_input()
        game.current_board[player_move] = 1
        print("\n")
        print_board(game.current_board)
        print("\n")
        game_over = game.is_game_over(game.current_board)
        if game_over in [-1, 1, 0]:
            print_board(game.current_board)
            print("\n")
            print_game_over_message_pve(game_over)
            break

        move = make_move(game, -1)
        print("Ai Move: ", move, "\n")
        game.current_board[move] = -1
        game_over = game.is_game_over(game.current_board)
        if game_over in [-1, 1, 0]:
            print_board(game.current_board)
            print("\n")
            print_game_over_message_pve(game_over)
            break


def p_v_p():  # why make something so small be pretty. if it works it works. there is no future for the project; i have no features i want to make.
    while True:
        print_board(game.current_board)
        print("\n")
        player_move = retrieve_player_input(1)
        game.current_board[player_move] = 1
        print("\n")
        print_board(game.current_board)
        print("\n")
        game_over = game.is_game_over(game.current_board)

        if game_over in [-1, 1, 0]:
            print_board(game.current_board)
            print("\n")
            print_game_over_message_pvp(game_over)
            break

        player_move = retrieve_player_input(-1)
        game.current_board[player_move] = -1
        print("\n")

        game_over = game.is_game_over(game.current_board)
        if game_over in [-1, 1, 0]:
            print_board(game.current_board)
            print("\n")
            print_game_over_message_pvp(game_over)
            break


def retrieve_player_input(player=None):
    msg = "Your Move: "
    if player == 1:
        msg = "Player One: "
    elif player == -1:
        msg = "Player Two: "
    move = input(msg)
    if move not in [str(move) for move in game.moves(game.current_board)]:
        print("Invalid Move.")
        return retrieve_player_input(player)
    return int(move)


def main():
    welcome_message = r"""
 _____ _        _____            _____
|_   _(_) ___  |_   _|_ _  ___  |_   _|__   ___
  | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \
  | | | | (__    | | (_| | (__    | | (_) |  __/
  |_| |_|\___|   |_|\__,_|\___|   |_|\___/ \___|

    """

    print(welcome_message)

    def game_mode():
        mode = input("How Many Players? (0-2): ")
        if mode not in [str(i) for i in range(3)]:
            print("Invalid Mode")
            return game_mode()
        return int(mode)

    mode = game_mode()

    print(r"""
 ____  _             _
/ ___|| |_ __ _ _ __| |_
\___ \| __/ _` | '__| __|
 ___) | || (_| | |  | |_
|____/ \__\__,_|_|   \__|

    """)
    if mode == 0:
        return ai_v_ai()
    elif mode == 1:
        return p_v_ai()
    elif mode == 2:
        return p_v_p()


if __name__ == "__main__":
    main()
