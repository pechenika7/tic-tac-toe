from players import player, computer1, computer2, human
from board import brd

class ttt():
    num_players = 2
    size = 5

    def __init__(self):
        self.board = brd(ttt.size)

    def SetPlayers(self, pl1, pl2):
        self.gamers = [pl1, pl2]

    def Play(self):
        f = open('logs.ttt', 'w')
        pls = [computer1('abc'), computer2('def'), human('hjk')]
        while True:
            self.board.ClearBoard()
            self.board.Draw()
            mq = 0 #количество ходов
            num = 0
            i1 = int(input('Choose first players. 0 - computer1, 1 - computer2, 2 - human'))
            i2 = int(input('Choose first players. 0 - computer1, 1 - computer2, 2 - human'))
            self.SetPlayers(pls[i1], pls[i2])
            f.write(str(self.gamers))
            while True:
                res = self.board.IsGameOver()
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
                self.board.Draw()
                num += 1
            is_end = int(input('Do u want to end? 0 - end'))
            if is_end == 0:
                break
        f.close()

p = ttt()
p.Play()