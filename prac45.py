# 1920 - 수 찾기

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()

m = int(input())
B = list(map(int, input().split()))

    
for num in B:
    result = False
    h = len(A) - 1
    l = 0
    while l <= h:
        mid = (h + l) // 2
        if num == A[mid]:
            result = True
            print(1)
            break
        elif num > A[mid]:
            l = mid + 1
        elif num < A[mid]:
            h = mid - 1
    if not result:
        print(0)
