# 1966 - 프린터 큐


import sys
input = sys.stdin.readline
from collections import deque

case = int(input())

for _ in range(case):
    n, m = map(int, input().split())
    important = deque(list(map(int, input().split())))
    
    count = 0
    while important:
        max_val = max(important)
        val = important.popleft()
        m -= 1
        if val == max_val:
            count += 1
            if m < 0:
                print(count)
                break
        else:
            important.append(val)
            if m < 0:
                m = len(important) - 1
