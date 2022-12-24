# 2252 - 줄 세우기

import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split()) # n : 학생 수, m : 키 재는 횟수
graph = [[] for _ in range(n+1)] # 위상정렬
people = [0] * (n+1) # 진입차수를 위한 변수
q = deque()

answer = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    people[b] += 1
    
for i in range(1, n+1):
    if people[i] == 0:
        q.append(i)
        
while q:
    p = q.popleft()
    answer.append(p)
    for i in graph[p]:
        people[i] -= 1
        if people[i] == 0:
            q.append(i)

print(*answer)