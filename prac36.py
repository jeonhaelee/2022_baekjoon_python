# 16564 - 히오스 프로게이머

import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
level_info = sorted([int(input()) for _ in range(n)])
                    
start = min(level_info)
end = max(level_info) + k

answer = 0
while start <= end:
    mid = (start + end) // 2
    
    x = 0
    for level in level_info:
        x += max(mid - level, 0)
        
    if x > k:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid
    
print(answer)