# 11497 - 통나무

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True) # 내림차순 정렬
    result = 0
    for i in range(n-2): # 내림차순 정렬을 해놨기 때문에, i와 i+1 관계는 확인 안 해주어도 됨!
        result = max(result, arr[i] - arr[i+2])
    print(result)
    