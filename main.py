from random import choice

class ttt():
    num_players = 2
    size = 5

    def __init__(self):
        self.board = list([None] * (ttt.size**2))
        self.players = ('computer1', 'computer1')

    def Draw1(self):
        for i in range(ttt.size - 1, -1, -1):
            print(self.board[ttt.size * i:ttt.size * i + ttt.size: 1])

    def Draw(self):
        for i in range(ttt.size - 1, -1, -1):
            b = list()
            for j in range(ttt.size):
                b.append(self.board[ttt.size * i + j])
            print(b)

    def ClearBoard(self):
        self.board = list([None] * (ttt.size**2))

    @classmethod
    def SetPlayers(cls):
        p_dict = {'h': 'human', 'c1': 'computer1', 'c2': 'computer2'}
        p1 = p_dict.get(input('Who will be first player? h - human, c1- computer1'))
        p2 = p_dict.get(input('Who will be second player? h - human, c1- computer1'))
        return (p1, p2)

    def IsValidMove(self, n):
        return (n < ttt.size**2) and (self.board[n] is None)

    def IsGameOver(self):

        for i in range(ttt.size):
            s = set()
            for j in range(ttt.size):
                s.add(self.board[i + j * ttt.size])
            if len(s) == 1:
                return s.pop()

        for i in range(ttt.size):
            s = set()
            for j in range(ttt.size):
                s.add(self.board[i * ttt.size +j])
            if len(s) == 1:
                return s.pop()

        s = {self.board[i] for i in range(0, ttt.size ** 2, ttt.size + 1)}
        if len(s) == 1:
            return s.pop()
        s = {self.board[i] for i in range(ttt.size - 1, (ttt.size * (ttt.size - 1) + 1), ttt.size - 1)}
        if len(s) == 1:
            return s.pop()

        return None

    def NextMove(self, item):
        if self.players[item] == 'computer1':
            indx = self.board.index(None)
        elif self.players[item] == 'computer2':
            list_ = list()
            for i in range(len(self.board)):
                if self.board[i] == None:
                    list_.append(i)
            indx = choice(list_)
        else: #for human
            while True:
                indx = int(input('Choose your move'))
                if ttt.IsValidMove(self, indx):
                    break
                else:
                    print('Incorrect move')
        self.board[indx] = bool(item)


    def Play(self):
        while True:
            ttt.ClearBoard(self)
            ttt.Draw1(self)
            mq = 0 #количество ходов
            num = 0
            if input('Do you want to choose players? Now: ' + str(self.players) + 'y - yes ') == 'y':
                self.players = ttt.SetPlayers()
            while True:
                res = ttt.IsGameOver(self)
                print(res)
                if res is None and mq == ttt.size**2:
                    print('Draw!')
                    break
                elif res is True:
                    print('Second player won up!')
                    break
                elif res is False:
                    print('First player won up!')
                    break
                ttt.NextMove(self, num%2)
                mq +=1
                ttt.Draw1(self)
                num +=1
            is_end = int(input('Do u want to end? 0 - end'))
            if is_end == 0:
                break

p = ttt()
p.Play()