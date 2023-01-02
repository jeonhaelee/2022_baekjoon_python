# 1987 - 알파벳

import sys

R, C = map(int, input().split())
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

vst = set([(0, 0, arr[0][0])])
answer = 1

while vst:
    x, y, visited = vst.pop()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] not in visited:
            vst.add((nx, ny, visited + arr[nx][ny]))
        answer = max(answer, len(visited))
            
print(answer)