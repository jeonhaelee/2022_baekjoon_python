# 1561 - 놀이 공원
# 시간 초과


import sys
input = sys.stdin.readline

def minus(li):
    for i in range(len(li)):
        if li[i] != 0:
            li[i] -= 1
    return li
        
n, m = map(int, input().split())
play = [*map(int, input().split())]
time_li = [0] * m

people = n
while people > 0:
    for t in range(m):
        if time_li[t] == 0:
            time_li[t] = play[t]
            if people - 1 == 0:
                print(t+1)
                sys.exit()
            people -= 1
    time_li = minus(time_li)

