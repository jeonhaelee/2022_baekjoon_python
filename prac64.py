# 2573 - 빙산

import sys
input = sys.stdin.readline

from collections import deque


n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 탐색을 위한 변수
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 남아있는 빙산이 있는지, 있다면 얼마나 남았는지 확인하고 업데이트 해주는 함수
def check_sea():
    melt_board = [[0]*m for _ in range(n)] # 빙산의 정보가 담긴 변수
    ice_left = 0 # 빙산이 남아 있는지 아닌지 확인을 위한 변수
    for i in range(n): # for문을 통해 빙산 전체를 확인해준다.
        for j in range(m):
            if ice[i][j] != 0: # 현재 위치에 빙산이 있을 때만 아래 코드를 진행한다.
                count = 0
                for k in range(4): # 상하좌우로 인접한 바다의 count를 세어준다.
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] == 0:
                        count += 1
                melt_board[i][j] = max(ice[i][j] - count, 0) # 원래의 빙산 숫자에서 인접한 바다의 count를 빼준다. 
                # (빙산의 숫자가 최소 0 이상이기 때문에 max 함수를 통해 음수값을 0 처리 해줌)
                ice_left += melt_board[i][j] # 업데이트 된 해당 빙산의 숫자를 ice_left에 더해줌
    if ice_left: # 빙산이 남아 있다면, melt_board와 함께 True를 리턴
        return melt_board, True
    else: # 빙산이 남아 있지 않다면, melt_board와 함께 False를 리턴
        return melt_board, False

# 빙산 뭉치의 개수를 확인 해주는 함수
def bfs():
    count = 0 # 빙산 뭉치 count를 위한 변수
    visited = [[False]*m for _ in range(n)] # 방문 확인을 위한 변수
    for i in range(n): # for문을 통해 빙산 전체를 확인해준다.
        for j in range(m):
            if ice[i][j] != 0 and not visited[i][j]: # 현재 위치에 빙산이 있거나 아직 방문하지 않았을 때만 아래 코드를 진행한다.
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
                count += 1 # 연결되어 있는 빙산 뭉치를 확인 해주었으면, 다음 빙산 뭉치를 또 확인해준다.
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