# 11657 - 타임머신

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bus_info = []
time_li = [1e9] * (n+1)

for _ in range(m):
    bus_info.append(list(map(int, input().split())))

time_li[1] = 0
for r in range(n):
    for s, e, t in bus_info:
        if time_li[s] != 1e9 and time_li[s] + t < time_li[e]:
            time_li[e] = time_li[s] + t
            if r == n-1:
                print(-1)
                sys.exit()
            
for i in range(2, n+1):
    if time_li[i] == 1e9:
        print(-1)
    else:
        print(time_li[i])
    