

class TicTacToe:
    def __init__(self, n):
        self.board = [[None] * n for i in range(n)]

    def move(self, row, col, player):
        self.board[row][col] = player
        if row == col and self.checkLeftDiag(player):
            return player

        if row + col == len(self.board) - 1 and self.checkRightDiag(player):
            return player

        if self.checkCol(col, player) or self.checkRow(row, player):
            return player

        return 0

    def checkCol(self, col, player):
        for i in range(len(self.board)):
            if self.board[i][col] != player:
                return False

    def checkRow(self, row, player):
        for i in range(len(self.board)):
            if self.board[row][i] != player:
                return False

    def checkLeftDiag(self, player):
        for i in range(len(self.board)):
            if self.board[i][i] != player:
                return False

    def checkRightDiag(self, player):
        for i in range(len(self.board)):
            if self.board[i][len(self.board)-i-1] != player:
                return False


new_solution = TicTacToe(3)
new_solution.move(1, 1, 1)
print(new_solution.board)
