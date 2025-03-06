class ttt():
    num_players = 2
    size = 3

    def __init__(self):
        self.board = list([None] * (ttt.size**2))
        self.players = ['human', 'computer']

    def Draw(self):
        print('draw a board')
        for i in range(2, -1, -1):
            print(self.board[3*i], self.board[3*i+1], self.board[3*i+2])

    def ClearBoard(self):
        self.board = list([None] * (ttt.size**2))

    def SetPlayers(self):
        p1 = 'human'
        p2 = 'computer'
        print(p1, p2)

    def IsValidMove(self, n):
        return (n < 9) and (self.board[n] is None)

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

    def NextMove(self, num):

        def CalcIndex(flag):
            if flag is True:
                return 0
            else:
                return 1


        if self.players[CalcIndex(num)] == 'computer':
            i = 0
            while True:
                if self.board[i] is None:
                    self.board[i] = num
                    break
                i += 1
        elif self.players[CalcIndex(num)] == 'human':
            while True:
                i = int(input('Choose your move'))
                if ttt.IsValidMove(self, i):
                    break
                else:
                    print('Incorrect move')
            self.board[i] = num


    def Play(self):
        while True:
            ttt.ClearBoard(self)
            ttt.Draw(self)
            mq = 0 #количество ходов
            num = True
            while True:
                res = ttt.IsGameOver(self)
                print(res)
                if res is None and mq == 9:
                    print('Draw!')
                    break
                elif res is True:
                    print('First player won up!')
                    break
                elif res is False:
                    print('Second player won up!')
                    break
                ttt.NextMove(self, num)
                mq +=1
                ttt.Draw(self)
                num = not num
            is_end = int(input('Do u want to end? 0 - end'))
            if is_end == 0:
                break

p = ttt()
p.Play()