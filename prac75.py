# 15810 - 풍선 공장

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
time = list(map(int, input().split()))

min_time = (m // n) * min(time)
max_time = (m // n + 1) * max(time)

answer = max_time
while min_time <= max_time:
    mid_time = (min_time + max_time) // 2
    
    count = 0
    for t in time:
        count += mid_time // t
        
    if count >= m:
        answer = mid_time
        max_time = mid_time - 1

    elif count < m:
        min_time = mid_time + 1
        
print(answer)