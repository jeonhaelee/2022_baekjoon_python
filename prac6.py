# 10157 - 자리배정

import sys

C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)
    sys.exit()
    
board = [[0]*C for _ in range(R)]
board[0][0] = 1

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
change = 0
x = 0; y = 0
for i in range(2, K+1):
    while True:
        a, b = move[change]
        dx = x + a; dy = y + b
        if R>dx>=0 and C>dy>=0 and board[dx][dy] == 0:
            board[dx][dy] = i
            x = dx; y = dy
            break
        else:
            change = (change+1) % 4


print(y+1, x+1)