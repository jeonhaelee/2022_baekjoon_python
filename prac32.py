# 11403 - 경로 찾기

import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 or (arr[i][k] == 1 and arr[k][j] == 1):
                arr[i][j] = 1

for a in arr:
    print(*a)
