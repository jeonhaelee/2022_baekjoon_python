# 16986 - 인싸들의 가위바위보

import sys
input = sys.stdin.readline

from itertools import permutations

N, K = map(int, input().split()) # N : 손동작 수, K : 우승을 위해 필요한 승수
arr = [list(map(int, input().split())) for _ in range(N)] # 상성에 대한 정보 배열

p_j = list(permutations([i for i in range(1, N+1)], N)) # 지우 <- N개의 손동작 수로 낼 수 있는 순열 
p_k = list(map(int, input().split())) # 경희
p_m = list(map(int, input().split())) # 민호


def find_next(p1, p2): # 현재 게임에 참여하지 않은 플레이어 리턴해주는 함수
    if 0 not in [p1, p2]:
        return 0
    if 1 not in [p1, p2]:
        return 1
    if 2 not in [p1, p2]:
        return 2
    
    
answer = 0
for jio in p_j:
    player = [jio, p_k, p_m]
    score = [0, 0, 0] # 점수 기록 리스트
    plan = [0, 0, 0] # 어떤 손동작 번호를 낼 지 기록 리스트
    p1, p2 = 0, 1 # 플레이어 1, 플레이어 2
    
    while K not in score:
        if plan[0] >= N or plan[1] >= 20 or plan[2] >= 20: # 지우가 모든 손동작을 쓴 경우와 다른 플레이어가 20경기가 지난 경우 while문 break
            break
        
        p1_result = player[p1][plan[p1]] # 플레이어 1의 손동작 번호
        p2_result = player[p2][plan[p2]] # 플레이어 2의 손동작 번호
        
        result = arr[p1_result - 1][p2_result -1 ] # 두 명의 손동작 번호의 상생 결과
        
        if result == 2: # 플레이어 1이 이긴 경우
            score[p1] += 1
            plan[p1] += 1
            plan[p2] += 1
            p2 = find_next(p1, p2)
            
        elif result == 1: # 비긴 경우 (더 뒷 번호인 사람이 이긴 것)
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
        
        else: # 플레이어 2가 이긴 경우
            score[p2] += 1
            plan[p1] += 1
            plan[p2] += 1
            p1 = find_next(p1, p2)
            
    if score[0] >= K: # 지우의 점수가 K 이상이면 answer = 1
        answer = 1
        
print(answer)