class brd():

    def __init__(self, size):
        self.size = size
        self.board = list([None] * (self.size**2))

    def __getitem__(self, item):
        return self.board[item]

    def __setitem__(self, key, value):
        self.board[key] = value

    def __index__(self):
        return self.board.index

    def Draw(self):
        for i in range(self.size - 1, -1, -1):
            print(self.board[self.size * i:self.size * i + self.size: 1])

    def ClearBoard(self):
        self.board = list([None] * (self.size**2))

    def IsGameOver(self):

        for i in range(self.size):
            s = set()
            for j in range(self.size):
                s.add(self.board[i + j * self.size])
            if len(s) == 1:
                return s.pop()

        for i in range(self.size):
            s = set()
            for j in range(self.size):
                s.add(self.board[i * self.size +j])
            if len(s) == 1:
                return s.pop()

        s = {self.board[i] for i in range(0, self.size ** 2, self.size + 1)}
        if len(s) == 1:
            return s.pop()
        s = {self.board[i] for i in range(self.size - 1, (self.size * (self.size - 1) + 1), self.size - 1)}
        if len(s) == 1:
            return s.pop()

        return None