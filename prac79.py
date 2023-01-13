# 1937 - 욕심쟁이 판다

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if visited[x][y]: return visited[x][y]

    visited[x][y] = 1      
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and forest[nx][ny] > forest[x][y]:
            visited[x][y] = max(dfs(nx, ny)+1, visited[x][y])
        
    return visited[x][y]

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))
        
print(answer)


#############################


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    if visited[x][y]: # 이미 방문한 곳이면 기록해뒀던 값으로 리턴
        return visited[x][y]
    
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and forest[nx][ny] > forest[x][y]:
            visited[x][y] = max(visited[x][y], bfs(nx, ny) + 1) 
        
    return visited[x][y]

answer = 0
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        answer = max(answer, bfs(i, j))
        
print(answer)
    


