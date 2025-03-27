from players import player, computer1, computer2, human

class ttt():
    num_players = 2
    size = 3

    def __init__(self):
        self.board = list([None] * (ttt.size**2))
        self.gamers = [computer2('ibm'), computer2('idl')]

    def Draw1(self):
        for i in range(ttt.size - 1, -1, -1):
            print(self.board[ttt.size * i:ttt.size * i + ttt.size: 1])

    def ClearBoard(self):
        self.board = list([None] * (ttt.size**2))

    @classmethod
    def SetPlayers(cls):
        p_dict = {'h': 'human', 'c1': 'computer1', 'c2': 'computer2'}
        p1 = p_dict.get(input('Who will be first player? h - human, c1- computer1'))
        p2 = p_dict.get(input('Who will be second player? h - human, c1- computer1'))
        return (p1, p2)

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
        while True:
            ttt.ClearBoard(self)
            ttt.Draw1(self)
            mq = 0 #количество ходов
            num = 0
           # if input('Do you want to choose players? Now: ' + str(self.gamers) + 'y - yes ') == 'y':
           #     self.gamers = ttt.SetPlayers()
           # f.write(str(self.gamers))
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