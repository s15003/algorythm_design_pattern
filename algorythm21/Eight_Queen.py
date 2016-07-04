# -*- coding: utf-8 -*-


class EQueen(object):
    def __init__(self, n):
        self.n = n
        self.pos = ['FREE'] * n
        self.col = ['FREE'] * n
        self.upwd = ['FREE'] * ((2 * n) + 1)
        self.downwd  = ['FREE'] * ((2 * n) + 1)

    def search(self, i):
        for k in range(0, self.n):
            if self.col[k] == 'FREE' and self.upwd[i+k] == 'FREE' and self.downwd[self.n+i-k-1] == 'FREE':
                self.pos[i] = k
                self.col[k] = 'NOT_FREE'
                self.upwd[i+k]  = 'NOT_FREE'
                self.downwd[self.n+i-k-1] = 'NOT_FREE'
                if i == self.n-1:
                    return 'SUCCESS'
                else:
                    if (self.search(i+1) == 'SUCCESS'):
                        return 'SUCCESS'
                    else:
                        #print 'クイーンを取り除く'
                        self.pos[i] = 0
                        self.col[k] = 'FREE'
                        self.upwd[i+k]  = 'FREE'
                        self.downwd[self.n+i-k-1] = 'FREE'

        return 'FAILURE'

    def disp(self):
        for i in range(0, self.n):
            for k in range(0, self.n):
                if self.pos[i] == k:
                    print 'Q'   ,
                else:
                    print '-',
            print ""

queen = EQueen(8) #ここの数値を変えることによって盤面を変えることができる

if queen.search(0) == 'SUCCESS':
    queen.disp()
