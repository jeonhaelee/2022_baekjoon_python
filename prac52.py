# 2961 - 도영이가 만든 맛있는 음식

import sys
input = sys.stdin.readline

from itertools import combinations

n = int(input())

get_item = []
for _ in range(n):
    s, ss = map(int, input().split())
    get_item.append([s, ss])


answer = 1e9
combi = []
for i in range(1, n+1):
    combi.append(combinations(get_item, i))

for coms in combi:
    for com in coms:
        sour = 1
        bitter = 0
        for c in com:
            sour *= c[0]
            bitter += c[1]
        result = abs(sour - bitter) 
        answer = min(answer, result)
    
print(answer)

