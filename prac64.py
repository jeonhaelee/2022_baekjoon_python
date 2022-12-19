# 2573 - 빙산

import sys
input = sys.stdin.readline

from collections import deque


n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check_sea():
    melt_board = [[0]*m for _ in range(n)]
    ice_left = 0
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0:
                count = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] == 0:
                        count += 1
                melt_board[i][j] = max(ice[i][j] - count, 0)
                ice_left += melt_board[i][j]
    if ice_left:
        return melt_board, True
    else:
        return melt_board, False


def bfs():
    count = 0
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0 and not visited[i][j]:
                q = deque()
                q.append([i, j])
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] != 0 and not visited[nx][ny]:
                            q.append([nx, ny])
                            visited[nx][ny] = True
                count += 1
    return count

ice_left = True
y_count = 0
while ice_left:
    ice, ice_left = check_sea()
    y_count += 1
    if bfs() >= 2:
        break

if ice_left:
    print(y_count)
else:
    print(0)