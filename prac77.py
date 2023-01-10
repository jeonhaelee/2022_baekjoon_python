# 1939 - 중량제한

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bridge = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bridge[a].append([b, c])
    bridge[b].append([a, c])
    
A, B = map(int, input().split())

def bfs(mid):
    q = deque()
    q.append(A)
    visited = [False] * (n+1)
    visited[A] = True
    
    while q:
        x = q.popleft()
        
        for i, w in bridge[x]:
            if not visited[i] and w >= mid:
                visited[i] = True
                q.append(i)
    
    if visited[B]:
        return True
    else:
        return False
    

start = 1
end = 1000000000

result = 0
while start <= end:
    mid = (start + end) // 2
    
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)