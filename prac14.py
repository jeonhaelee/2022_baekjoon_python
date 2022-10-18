# 17836 - 공주님을 구해라

import sys
from collections import deque
imput = sys.stdin.readline


def bfs(x, y, dst_x, dst_y, time):
    q = deque([(x, y, time)])
    visited = [[0] * m for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while q:
        x, y, time = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 1 and visited[nx][ny] == 0:
                if nx == dst_x and ny == dst_y:
                    return time + 1
                q.append((nx, ny, time + 1))
                visited[nx][ny] = 1
    return float('inf')


n, m, t = map(int, input().split())

board = [[] for _ in range(n)]

for i in range(n):
    board[i] = list(map(int, input().split()))
    if 2 in board[i]:
        knife = [i, board[i].index(2)]
        
not_use_knife = bfs(0, 0, n-1, m-1, 0)
tmp = bfs(0, 0, knife[0], knife[1], 0)

if tmp!= float('inf'):
    use_knife = tmp + abs(n-1-knife[0]) + abs(m-1-knife[1])
else:
    use_knife = tmp

result = min(not_use_knife, use_knife)
print(result if result <= t else "Fail")
