# 11497 - 통나무

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    result = 0
    for i in range(n-2):
        result = max(result, arr[i] - arr[i+2])
    print(result)
    