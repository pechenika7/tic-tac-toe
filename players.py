from random import choice

class player():

    def __init__(self, name, bd):
        self.name = name
        self.board = bd

    def IsValidMove(self, n):
        return True

    def UpdateBoard(self, bd):
        self.board = bd

class computer1(player):

    def __init__(self, name, bd):
        super().__init__(name, bd)

    def NextMove(self):
        print('computer 1')
        return self.board.index(None)


class computer2(player):

    def __init__(self, name, bd):
        super().__init__(name, bd)

    def NextMove(self):
        print('computer 2')
        list_ = list()
        for i in range(len(self.board)):
            if self.board[i] is None:
                list_.append(i)
        return choice(list_)


class human(player):

    def __init__(self, name):
        super().__init__(name, bd)

    def IsValidMove(self, n):
        return (n < ttt.size**2) and (self.board[n] is None)

    def NextMove(self):
        print('human')
        while True:
            indx = int(input('Choose your move'))
            if ttt.IsValidMove(self, indx):
                return indx
            else:
                print('Incorrect move')
