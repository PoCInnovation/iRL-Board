class TicTacToe:
    def __init__(self):
        self.board = [[0, 0, 0] for _ in range(3)]
        self.player = 1

    def copy(self):
        copy = TicTacToe()
        copy.board = [row[:] for row in self.board]
        copy.player = self.player
        return copy

    def get_valid_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0]

    def make_move(self, move):
        i, j = move
        if self.board[i][j] != 0:
            raise ValueError('Invalid move')
        self.board[i][j] = self.player

        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def get_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[0][2]
        # No winner yet
        return 0

    def show_board(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    print(' ', end='')
                elif self.board[i][j] == 1:
                    print('X', end='')
                else:
                    print('O', end='')
                if j < 2:
                    print('|', end='')
            print()
            if i < 2:
                print('-----')
        print()


if __name__ == '__main__':
    game = TicTacToe()
    error = True

    while game.get_winner() == 0:
        while error == True:
            print('Player', game.player)
            game.show_board()
            entry = input('Enter row, column: ')
            entry.strip()
            if entry.find(',') == -1:
                print('Invalid move')
                error = True
                continue
            i, j = entry.split(',')
            try:
                game.make_move((int(i), int(j)))
                error = False
            except ValueError:
                print('Invalid move')
                error = True
        error = True
    game.show_board()
    print('Player', game.get_winner(), 'wins!')