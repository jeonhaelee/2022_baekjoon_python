# 1253 - 좋다

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

answer = 0
for i in range(n):
    check_arr = arr[:i] + arr[i+1:]
    left = 0; right = len(check_arr) - 1
    while left < right:
        if check_arr[left] + check_arr[right] == arr[i]:
            answer += 1
            break
        elif check_arr[left] + check_arr[right] < arr[i]:
            left += 1
        elif check_arr[left] + check_arr[right] > arr[i]:
            right -= 1
            
print(answer)