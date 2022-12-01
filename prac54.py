# 16986 - 인싸들의 가위바위보

import sys
input = sys.stdin.readline

from itertools import permutations

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

p_j = list(permutations([i for i in range(1, N+1)], N))
p_k = list(map(int, input().split()))
p_m = list(map(int, input().split()))


def find_next(p1, p2):
    if 0 not in [p1, p2]:
        return 0
    if 1 not in [p1, p2]:
        return 1
    if 2 not in [p1, p2]:
        return 2
    
    
answer = 0
for jio in p_j:
    player = [p_j, p_k, p_m]
    score = [0, 0, 0]
    plan = [0, 0, 0]
    p1, p2 = 0, 1
    
    while K not in score:
        if plan[0] >= N or plan[1] >= 20 or plan[2] >= 20:
            break
        
        p1_result = player[p1][plan[p1]]
        p2_result = player[p2][plan[p2]]
        
        result = arr[p1_result - 1][p2_result -1 ]
        
        if result == 2:
            score[p1] += 1
            plan[p1] += 1
            plan[p2] += 1
            p2 = find_next(p1, p2)
            
        elif result == 1:
            if p1 < p2:
                score[p2] += 1
                plan[p1] += 1
                plan[p2] += 1
                p1 = find_next(p1, p2)
            else:
                score[p1] += 1
                plan[p1] += 1
                plan[p2] += 1
                p2 = find_next(p1, p2)
        
        else:
            score[p2] += 1
            plan[p1] += 1
            plan[p2] += 1
            p1 = find_next(p1, p2)
            
if score[0] >= K:
    answer = 1
        
print(answer)