# 1238 - 파티

import sys
input = sys.stdin.readline
import heapq
import math

n, m, x = map(int, input().split()) # 학생 수(집 수), 도로 수, 파티하는 장소
load = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    load[s].append([t, e])


def get_distance(s_node): 
    # node를 입력받으면, 이 node부터 다른 각 node까지의 최단 경로 시간을 구해준다.
    distance = [math.inf] * (n+1)
    q = []
    heapq.heappush(q, (0, s_node)) # (소요 시간, 연결 노드)
    distance[s_node] = 0
    
    while q:
        time, node = heapq.heappop(q)
        for next_time, next_node in load[node]:
            # heapq.heappush(q, [next_time, next_node])
            # distance[next_node] = min(time + next_time, distance[next_node])
            if distance[next_node] > (time + next_time):
                distance[next_node] = time + next_time
                heapq.heappush(q, (time + next_time, next_node))
    
    return distance

answer = [0] * (n+1)
for i in range(1, n+1):
    dist = get_distance(i)
    answer[i] += dist[x]
    dist2 = get_distance(x)
    answer[i] += dist2[i]
    
print(max(answer))
    