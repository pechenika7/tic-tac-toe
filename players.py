from random import choice

class player ():

    def __init__(self, name):
        self.name = name

    def IsValidMove(self, n, board=None):
        return True


class computer1 (player):

    def __init__(self, name):
        super().__init__(name)

    def NextMove(self, board):
        print('computer 1')
        return board.index(None)


class computer2 (player):

    def __init__(self, name):
        super().__init__(name)

    def NextMove(self, board):
        print('computer 2')
        list_ = list()
        for i in range(len(board)):
            if board[i] is None:
                list_.append(i)
        return choice(list_)


class human(player):

    def __init__(self, name):
        super().__init__(name)

    def IsValidMove(self, n, board):
        return (n < len(board)**2) and (board[n] is None)

    def NextMove(self, board):
        print('human')
        while True:
            indx = int(input('Choose your move'))
            if self.IsValidMove(indx, board):
                return indx
            else:
                print('Incorrect move')
