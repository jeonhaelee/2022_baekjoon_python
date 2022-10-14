# 1743 - 음식물 피하기


from collections import deque


N, M, K = map(int, input().split())
floor = [[0] * M for _ in range(N)]

for _ in range(K):
    i, j = map(int, input().split())
    floor[i-1][j-1] = 1
    
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def finder(i, j, floor):
    q = deque([[i, j]])
    floor[i][j] = 2
    result = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and floor[nx][ny] == 1:
                q.append([nx, ny])
                floor[nx][ny] = 2
                result += 1
    return result
    

answer = 0
for i in range(N):
    for j in range(M):
        if floor[i][j] == 1:
            ans = finder(i, j, floor)
            answer = max(answer, ans)
            
print(answer)