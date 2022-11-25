# 16439 - 치킨치킨치킨

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
like = [list(map(int,input().split())) for _ in range(n)]

chicken_combinations = combinations(range(m), 3)

answer = 0
for c1, c2, c3 in chicken_combinations:
    max_like = 0
    for i in range(n):
        max_like += max(like[i][c1], like[i][c2], like[i][c3])
    answer = max(answer, max_like)
    
print(answer)