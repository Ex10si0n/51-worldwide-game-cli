from helper import *

class Game:
    def __init__(self):
        self.board = [[0] * 7 for _ in range(6)]
        self.turn = 1
        self.start()

    def print_board(self):
        cls()
        print(' '*6, end='')
        for col in range(len(self.board[0])):
            render(str(col+1), 'r', '.', end='↓ ')
        print('')
        for row in range(len(self.board)):
            render(str(row+1), 'c', '.', end=' '*3)
            for col in range(-1, len(self.board[row])+1):
                if col == -1:
                    print('|', end=' ')
                    continue
                if col == len(self.board[row]):
                    print('|', end='')
                    continue
                if self.board[row][col] == 0:
                    render('..', '..', '11', end=' ')
                if self.board[row][col] == 1:
                    render('11', '..', 'rr', end=' ')
                if self.board[row][col] == 2:
                    render('22', '..', 'yy', end=' ')
            print()

    def place_col(self, col, player):
        for row in range(len(self.board)-1, -1, -1):
            if self.board[row][col-1] == 0:
                self.board[row][col-1] = player
                return

    def check_win(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    continue
                if self.board[row][col] == self.turn:
                    if row+4 < len(self.board):
                        if self.board[row+1][col] == self.turn and self.board[row+2][col] == self.turn and \
                                self.board[row+3][col] == self.turn and self.board[row+4][col] == self.turn:
                            return True
                    if col+4 < len(self.board[row]):
                        if self.board[row][col+1] == self.turn and self.board[row][col+2] == self.turn and \
                                self.board[row][col+3] == self.turn and self.board[row][col+4] == self.turn:
                            return True
                    if row-4 >= 0:
                        if self.board[row-1][col] == self.turn and self.board[row-2][col] == self.turn and \
                                self.board[row-3][col] == self.turn and self.board[row-4][col] == self.turn:
                            return True
                    if col-4 >= 0:
                        if self.board[row][col-1] == self.turn and self.board[row][col-2] == self.turn and \
                                self.board[row][col-3] == self.turn and self.board[row][col-4] == self.turn:
                            return True
                    if row+4 < len(self.board) and col+4 < len(self.board[row]):
                        if self.board[row+1][col+1] == self.turn and self.board[row+2][col+2] == self.turn and \
                                self.board[row+3][col+3] == self.turn and self.board[row+4][col+4] == self.turn:
                            return True
                    if row-4 >= 0 and col-4 >= 0:
                        if self.board[row-1][col-1] == self.turn and self.board[row-2][col-2] == self.turn and \
                                self.board[row-3][col-3] == self.turn and self.board[row-4][col-4] == self.turn:
                            return True
                    if row+4 < len(self.board) and col-4 >= 0:
                        if self.board[row+1][col-1] == self.turn and self.board[row+2][col-2] == self.turn and \
                                self.board[row+3][col-3] == self.turn and self.board[row+4][col-4] == self.turn:
                            return True
                    if row-4 >= 0 and col+4 < len(self.board[row]):
                        if self.board[row-1][col+1] == self.turn and self.board[row-2][col+2] == self.turn and \
                        self.board[row-3][col+3] == self.turn and self.board[row-4][col+4] == self.turn:
                            return True
        return False



    def start(self):
        self.print_board()
        while True:
            self.turn = 1
            while True:
                col = int(input('Player 1, choose a column: '))
                if col < 1 or col > 7:
                    print('Invalid column')
                    continue
                if self.board[0][col-1] != 0:
                    print('Column is full')
                    continue
                break
            self.place_col(col, 1)
            self.print_board()
            self.turn = 2
            while True:
                col = int(input('Player 2, choose a column: '))
                if col < 1 or col > 7:
                    print('Invalid column')
                    continue
                if self.board[0][col-1] != 0:
                    print('Column is full')
                    continue
                break
            self.place_col(col, 2)
            self.print_board()
            if self.check_win():
                print('Player', self.turn, 'wins!')
                break


if __name__ == "__main__":
    game = Game()
