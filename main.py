class tic_tac_toe():
    num_players = 2
    size = 3

    def __init__(self):
        self.board = list([None] * (tic_tac_toe.size**2))

    def Draw(self):
        print('draw a board')

    def SetPlayers(self):
        p1 = 'human'
        p2 = 'computer'
        print(p1, p2)

    def IsGameOver(self):
        for i in range(3):
            s = {self.board[0+i*3], self.board[1+i*3], self.board[2+i*3]}
            if len(s) == 1:
                return s.pop()
            s = {self.board[0+i], self.board[3+i], self.board[6+i]}
            if len(s) == 1:
                return s.pop()

        s = {self.board[0], self.board[4], self.board[8]}
        if len(s) == 1:
            return s.pop()
        s = {self.board[2], self.board[4], self.board[6]}
        if len(s) == 1:
            return s.pop()
        return None

p = tic_tac_toe()
p.board = [True, None, None, None, True, None, None, None, True]
print(p.IsGameOver())