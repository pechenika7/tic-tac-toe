from random import choice

class player ():

    def __init__(self, name):
        self.name = name

    def IsValidMove(self, n, b=None):
        return True


class computer1 (player):

    def __init__(self, name):
        super().__init__(name)

    def NextMove(self, b):
        print('computer 1')
        return b.board.index(None)


class computer2 (player):

    def __init__(self, name):
        super().__init__(name)

    def NextMove(self, b):
        print('computer 2')
        list_ = list()
        for i in range(len(b.board)):
            if b.board[i] is None:
                list_.append(i)
        return choice(list_)


class human(player):

    def __init__(self, name):
        super().__init__(name)

    def IsValidMove(self, n, b):
        return (n < len(b.board)**2) and (b.board[n] is None)

    def NextMove(self, b):
        print('human')
        while True:
            indx = int(input('Choose your move'))
            if self.IsValidMove(indx, b):
                return indx
            else:
                print('Incorrect move')
