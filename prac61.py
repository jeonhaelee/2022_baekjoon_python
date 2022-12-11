# 2239 - 스도쿠

import sys
input = sys.stdin.readline

board = [list(map(int, input().rstrip())) for _ in range(9)] # board 입력받기

visited_row = [[0]*9 for _ in range(9)] # 각 row의 숫자 유무 확인을 위한 변수
### 예) 첫번째 행 : board의 첫번째 행에 존재하는 숫자(1~9) 파악을 위한 행
### visited_row[0][0] = 1이면 board의 첫번째 행에 1 숫자가 존재한다는 뜻!
visited_col = [[0]*9 for _ in range(9)] # 각 col의 숫자 유무 확인을 위한 변수
visited_box = [[0]*9 for _ in range(9)] # 각 box의 숫자 유무 확인을 위한 변수

box = lambda i, j: i // 3 * 3 + (j // 3) # 해당 좌표가 몇번째 박스에 속하는 지

for i in range(9):
    for j in range(9):
        if board[i][j]: # 이미 채워져 있는 좌표 확인해서 visited 체크 해주기
            visited_row[i][board[i][j]-1] = 1
            visited_col[j][board[i][j]-1] = 1
            visited_box[box(i, j)][board[i][j]-1] = 1
            
def dfs(i, j):
    if i == 9: # 마지막 행이면 종료
        return 1

    if board[i][j]: # 현재 좌표에 이미 숫자가 있다면 다음 좌표로 이동
        return dfs(i + (j + 1) // 9, (j + 1) % 9)
        
    for c in range(9):
        if visited_row[i][c] or visited_col[j][c] or visited_box[box(i, j)][c]: # 해당 숫자가 이미 존재한다면 continue
            continue
        board[i][j] = c + 1 # 해당 좌표에 숫자를 넣어주기
        visited_row[i][c] = visited_col[j][c] = visited_box[box(i, j)][c] = 1 # visited도 체크해주기
        if dfs(i + (j + 1) // 9, (j + 1) % 9): # 마지막 행까지 숫자가 다 채워지면 종료
            return 1
        board[i][j] = 0 # 아니라면 다시 원복
        visited_row[i][c] = visited_col[j][c] = visited_box[box(i, j)][c] = 0 # visited도 원복
        
    return 0

dfs(0, 0) # 좌표 0, 0부터 dfs 시작!
for row in board: # 숫자가 다 채워진 최종 board 출력
    print(*row, sep="")

