# 1766 - 문제집

import sys
input = sys.stdin.readline

import heapq

n, m = map(int, input().split())
people = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    people[b] += 1
    
que = []
answer = []

for i in range(1, n+1):
    if people[i] == 0:
        heapq.heappush(que, i)
        
while que:
    p = heapq.heappop(que)
    for k in graph[p]:
        people[k] -= 1
        if people[k] == 0:
            heapq.heappush(que, k)
    answer.append(p)

print(*answer)
