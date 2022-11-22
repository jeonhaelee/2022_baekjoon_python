# 1516 - 게임 개발

from collections import deque

import sys
input = sys.stdin.readline

n = int(input())
building = [[] for _ in range(n+1)] # 각 인덱스 빌딩이 지어져야, 지어질 수 있는 빌딩들 모임
indegree = [0] * (n+1) # 지어지기 위해 먼저 지어져야 할 빌딩 개수
cost = [0] * (n+1) # 각 빌딩이 지어지는데 걸리는 시간

for i in range(1, n+1): # for문 돌면서 각 변수에 정보 넣어주기
    info = list(map(int, input().split()))[:-1] # 맨 마지막 -1 빼고 info에 담기
    cost[i] = info[0] # 첫번째 값은 해당 빌딩이 지어지는데 걸리는 시간
    building_info = info[1:] # 해당 빌딩이 지어지기 위해 먼저 지어져야 하는 빌딩들
    
    for b in building_info: # 먼저 지어져야 하는 빌딩들 돌면서 각 변수에 정보 추가
        building[b].append(i) # 
        indegree[i] += 1

answer = [0] * (n+1) # 해당 빌딩을 짓는데 걸리는 총 시간을 담을 변수
q = deque()

for i in range(1, n+1): # 선행으로 지어져야 할 빌딩이 없다면 q에 넣어줌
    if indegree[i] == 0:
        q.append(i)
        
while q:
    item = q.popleft()
    answer[item] += cost[item] 
    # 선행으로 지어져야 할 빌딩이 없으므로 해당 빌딩을 짓는데 걸리는 시간을 최종으로 더해줌
    
    for b in building[item]: # 해당 빌딩이 지어져야 지어질 수 있는 빌딩들 확인하면서 indegree -1씩 해줌
        indegree[b] -= 1
        answer[b] = max(answer[b], answer[item]) # 둘중의 max값으로 걸리는 시간 업데이트
        if indegree[b] == 0: # 다시 indegree가 0인 빌딩 확인해서 q에 넣어줌
            q.append(b)
            
for i in range(1, n+1): # 해당 빌딩 번호를 인덱스로 answer 돌면서 총 걸리는 시간 출력
    print(answer[i])