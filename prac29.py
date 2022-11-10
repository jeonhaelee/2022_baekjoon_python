# 1915 - 가장 큰 정사각형

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
check_arr = [[0]*m for _ in range(n)]

for _ in range(n):
    arr.append(list(input()))

def checking(x, y):
    if x > 0 and x < n and y > 0 and y < m:
        l = int(check_arr[x][y-1])
        u = int(check_arr[x-1][y])
        lu = int(check_arr[x-1][y-1])
        
        return min(l, u, lu) + 1
    
    else: return 1

answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '1':
            check_result = checking(i, j)
            check_arr[i][j] = check_result
            answer = max(answer, check_result)


print(answer**2)