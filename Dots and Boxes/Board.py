from random import *


class Game:
    def __init__(self, board, board_x, board_y):
        self.board = board
        self.board_x = board_x
        self.board_y = board_y

    # generating the weighted boxes
    def initiate(self):
        for i in range(0, self.board_y):
            lst = []
            for j in range(0, self.board_x):
                if i % 2 == 1 and j % 2 == 1:
                    lst.append(randint(1, 5))
                elif i % 2 == 0 and j % 2 == 0:
                    lst.append('*')
                else:
                    lst.append(' ')
            self.board.append(lst)

    # board matrix
    def get_matrix(self):
        result = []
        for i in range(0, self.board_y):
            lst = []
            for j in range(0, self.board_x):
                lst.append(self.board[i][j])
            result.append(lst)
        return result

    # drawing the board
    def draw_board(self):
        print()
        if self.board_x > 9:
            print(" ", end='')
        print("  ", end='')
        for i in range(0, self.board_x):
            print(str(i), end='  ')
        print()

        if self.board_x > 9:
            print(" ", end='')
        print("  ", end='')
        for i in range(0, self.board_x):
            if i == self.board_x-1:
                print("_", end='')
            else:
                print("___", end='')
        print()
        for j in range(self.board_y):
            if self.board_x > 9 and j < 10:
                print(" ", end='')
            print(str(j)+"|", end='')
            for z in range(self.board_x):
                print(str(self.board[j][z]), end='  ')
            print()
        print()

    # getting the current state of the game
    def get_state(self):
        return Game(self.get_matrix(), self.board_x, self.board_y)

    # exerting the move the human or ai played
    def action(self, i, j):
        sum = 0

        if j % 2 == 0 and i % 2 == 1:
            self.board[j][i] = '-'
            if j < self.board_y - 1:
                if self.board[j+2][i] == '-' and self.board[j+1][i+1] == '|' and self.board[j+1][i-1] == '|':
                    sum += self.board[j+1][i]
            if j > 0:
                if self.board[j-2][i] == '-' and self.board[j-1][i+1] == '|' and self.board[j-1][i-1] == '|':
                    sum += self.board[j-1][i]

        else:
            self.board[j][i] = '|'
            if i < self.board_x - 1:
                if self.board[j][i+2] == '|' and self.board[j+1][i+1] == '-' and self.board[j-1][i+1] == '-':
                    sum += self.board[j][i+1]
            if i > 0:
                if self.board[j][i-2] == '|' and self.board[j+1][i-1] == '-' and self.board[j-1][i-1] == '-':
                    sum += self.board[j][i-1]
        return sum