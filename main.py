from players import player, computer1, computer2, human

class ttt():
    num_players = 2
    size = 3

    def __init__(self):
        self.board = list([None] * (ttt.size**2))

    def Draw1(self):
        for i in range(ttt.size - 1, -1, -1):
            print(self.board[ttt.size * i:ttt.size * i + ttt.size: 1])

    def ClearBoard(self):
        self.board = list([None] * (ttt.size**2))

    def SetPlayers(self, pl1, pl2):
        self.gamers = [pl1, pl2]

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


    def Play(self):
        f = open('logs.ttt', 'w')
        pls = [computer1('abc'), computer2('def'), human('hjk')]
        while True:
            ttt.ClearBoard(self)
            ttt.Draw1(self)
            mq = 0 #количество ходов
            num = 0
            i1 = int(input('Choose first players. 0 - computer1, 1 - computer2, 2 - human'))
            i2 = int(input('Choose first players. 0 - computer1, 1 - computer2, 2 - human'))
            self.SetPlayers(pls[i1], pls[i2])
            f.write(str(self.gamers))
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
                n = self.gamers[num % 2].NextMove(self.board)
                self.board[n] = bool(num % 2)
                mq += 1
                ttt.Draw1(self)
                num += 1
            is_end = int(input('Do u want to end? 0 - end'))
            if is_end == 0:
                break
        f.close()

p = ttt()
p.Play()