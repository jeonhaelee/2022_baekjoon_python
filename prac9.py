# 15787 - 기차가 어둠을 헤치고 은하수를

import sys


N, M = map(int, input().split())

train = [0 for _ in range(N)]

seat_limit = 20
num_limit = 1 << seat_limit

for _ in range(M):
    order = list(map(int, sys.stdin.readline().split()))
    t_n = order[1] - 1
    
    if order[0] == 1:
        seat = order[2] - 1
        train[t_n] = train[t_n] | (1 << seat)
    elif order[0] == 2:
        seat = order[2] - 1
        train[t_n] = train[t_n] & ~(1 << seat)
    elif order[0] == 3:
        train[t_n] = (train[t_n] << 1) % num_limit
    else:
        train[t_n] = train[t_n] >> 1
        
started = set(train)
print(len(started))