"""
0s will always represent neutral (game draw, empy square)
1s will always represent Xs (X wins, X is on a square)
-1s will always represent 0s (O wins, O is on a square)
X will always move first
X is always the player
"""


class Game:
    def __init__(self) -> None:
        # Initial state is completly empty
        self.current_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        ROW_1 = [0, 1, 2]
        ROW_2 = [3, 4, 5]
        ROW_3 = [6, 7, 8]

        COLUMN_1 = [0, 3, 6]
        COLUMN_2 = [1, 4, 7]
        COLUMN_3 = [2, 5, 8]

        DIAG_1 = [2, 4, 6]
        DIAG_2 = [0, 4, 8]

        self.WIN_CONDITIONS = [
            ROW_1,
            ROW_2,
            ROW_3,
            COLUMN_1,
            COLUMN_2,
            COLUMN_3,
            DIAG_1,
            DIAG_2,
        ]

    def whos_turn(self, board):
        if board.count(0) == 9:
            return 1
        elif board.count(1) == board.count(-1):
            return 1
        return -1

    def moves(self, board):
        return [index for index, space in enumerate(board) if space == 0]

    def result(self, board, move):
        if board[move] != 0:
            raise Exception("Result was passed in a move that is not empty")

        player = self.whos_turn(board)
        new_board = board.copy()
        new_board[move] = player
        return new_board

    def is_game_over(self, board):
        """
        Functions as a Utility and a Terminal. if is_game_over returns False then games not over, but if it returns 1,-1, or 0 then the game is over
        (with those numbers repersenting their respective sides)
        """
        for indexs in self.WIN_CONDITIONS:
            if self.indexs_are_same_player(board, indexs):
                return board[
                    indexs[0]
                ]  # Could be errornoues if indexs_are_same_player fails

        if board.count(0) == 0:  # game is a draw
            return 0

        return None

    def indexs_are_same_player(self, board, indexs):
        if len(indexs) != 3:
            raise Exception("The list of indexs are not 3. how?")

        moves = [board[index] for index in indexs]
        if moves.count(-1) == 3 or moves.count(1) == 3:
            return True
        return False


def print_board(board):
    symbols = {
        1: "X",
        -1: "O",
        0: "",
    }  # 0 is place holder will be replaced with an space index

    for row in range(3):
        start = 3 * row
        cells = [
            symbols[board[start + i]] if symbols[board[start + i]] else str(start + i)
            for i in range(3)
        ]

        print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
        if row < 2:
            print("-----------")
