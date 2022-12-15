# 1194 - 달이 차오른다, 가자.

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split()) # n : 행 길이, m : 열 길이
arr = [list(input()) for _ in range(n)] # 미로

start_x = 0; start_y = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '0':
            start_x = i; start_y = j # '0'이 있는 좌표 = 시작점
            arr[i][j] = '.'
            break

# 딕셔너리로 각 알파벳에 해당하는 shift할 숫자 정의
alphabet = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5,
            'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5} 

# 상하좌우 탐색을 위해
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# '0'이 있는 좌표부터 시작
def bfs(x, y):
    q = deque([(x, y, 0, 0)])
    # 다녀간 자리인지 파악해주기 위한 check 변수
    check = [[[False] * (1 << 6) for _ in range(50)] for _ in range(50)]
    check[x][y][0] = True # 시작 위치는 True로 설정
    
    while q:
        x, y, count, key = q.popleft()
        if arr[x][y] == '1': # 미로 탈출 시 count값 리턴
            return count
        for k in range(4): # 상하좌우 확인
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if not check[nx][ny][key]:
                    if arr[nx][ny] == '1' or arr[nx][ny] == '.':
                        check[nx][ny][key] = True
                        q.append((nx, ny, count+1, key))
                    elif arr[nx][ny] in ('a', 'b', 'c', 'd', 'e', 'f'): # 열쇠
                        tmp_key = key | (1 << alphabet[arr[nx][ny]]) # 열쇠 추가
                        check[nx][ny][tmp_key] = True
                        q.append((nx, ny, count+1, tmp_key))
                    elif arr[nx][ny] in ('A', 'B', 'C', 'D', 'E', 'F'): # 문
                        if key & (1 << alphabet[arr[nx][ny]]): # 문을 열 수 있다면 (열쇠를 갖고 있다면)
                            check[nx][ny][key] = True
                            q.append((nx, ny, count+1, key))
                            
    return -1 # 미로를 탈출하지 못할 경우

answer = bfs(start_x, start_y)
print(answer)

