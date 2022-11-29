# 1007 - 벡터매칭

import sys
input = sys.stdin.readline

from itertools import combinations

T = int(input())

for _ in range(T):
    
    N = int(input())
    node = []
    total_x, total_y = 0, 0
    for _ in range(N):
        x, y = map(int, input().split())
        total_x += x; total_y += y
        node.append([x, y])
        
    combi = list(combinations(node, N//2))
    answer = 3e5
    
    for c in combi[:len(combi)//2]:
        x1, y1 = 0, 0
        for x, y in c:
            x1 += x; y1 += y
        x2, y2 = total_x - x1, total_y - y1
        sum_vector = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
        answer = min(answer, sum_vector)
        
    print(answer)
