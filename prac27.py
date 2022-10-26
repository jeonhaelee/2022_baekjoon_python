# 10815 - 숫자 카드

import sys
input = sys.stdin.readline

n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
numbers = list(map(int, input().split()))


for number in numbers:
    low, high = 0, n-1
    result = False
    while low <= high:
        mid = (low + high) // 2
        if cards[mid] > number:
            high = mid - 1
        elif cards[mid] < number:
            low = mid + 1
        else:
            result = True
            break
    if result:
        print(1, end = ' ')
    else: print(0, end = ' ')
        


