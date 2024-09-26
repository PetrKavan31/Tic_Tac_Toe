class TicTacToe:
    def __init__(self):
        self.board = ["."] * 9
        self.player_on_turn = 'X'
        self.winner = None

    def get_winner(self) -> str:
        return self.winner

    def is_over(self):
        return self.winner is not None or self.board.count('.') == 0

    def is_winner(self, player: str) -> bool:
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)]
        for indices in lines:
            if self.board[indices[0]] == player and self.board[indices[1]] == player and self.board[indices[2]] == player:
                return True
        return False

    def make_move(self, position: int):
        assert 0 <= position <= 8
        assert self.is_move_valid(position)
        self.board[position] = self.player_on_turn
        if self.is_winner(self.player_on_turn):
            self.winner = self.player_on_turn
        self.player_on_turn = 'X' if self.player_on_turn == 'O' else 'O'

    def is_move_valid(self, position: int) -> bool:
        assert 0 <= position <= 8
        return self.board[position] == '.'

######################################
# VIEW


def draw_board(board: list[str]):
    for i in range(0,9,3):
        print("".join(board[i:(i+3)]))


def get_user_input(game: TicTacToe) -> int:
    while True:
        player_on_turn = game.player_on_turn
        position = None
        try:
            position = int(input(f"Player {player_on_turn} turn. Enter the position (1-9): "))
            if position in range(1, 10) and game.is_move_valid(position - 1):
                return position - 1
        except ValueError:
            pass

        draw_board(game.board)
        if position in range(1, 10):
            print("Tile is covered.")
        else:
            print("Wrong number.")


def main():
    game = TicTacToe()
    while not game.is_over():
        draw_board(game.board)
        position = get_user_input(game)
        game.make_move(position)
    draw_board(game.board)
    if game.winner == 'X':
        print("The winner is player X.")
    elif game.winner == 'O':
        print("The winner is player O.")
    else:
        print("Nobody won.")
    print("End of game.")


if __name__ == "__main__":
    main()
