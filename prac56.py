# 1455 - 뒤집기

import sys

def flip(x):
    return (x+1)%2

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, list(sys.stdin.readline().rstrip()))))

answer = 0
for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        if arr[i][j] == 1:
            answer += 1
            for k in range(i, -1, -1):
                arr[k][:j+1] = list(map(flip, arr[k][:j+1]))
                
print(answer)