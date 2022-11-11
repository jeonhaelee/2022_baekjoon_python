# 1106 - 호텔

import sys
input = sys.stdin.readline

c, n = map(int, input().split())
money = [1e9] * (2000)

ad_info = []
for _ in range(n):
    ad_info.append(list(map(int, input().split())))
    
money[0] = 0
for cost, people in ad_info:
    for i in range(people, c+100):
        money[i] = min(money[i-people] + cost, money[i])

print(min(money[c:]))