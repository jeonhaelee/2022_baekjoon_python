# 1654 - 랜선 자르기

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]

start = 1
end = max(lans)

answer = 0
while start <= end:
    
    cnt = 0
    mid = (start + end) // 2
    for lan in lans:
        cnt += lan // mid
        
    if cnt >= n:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(answer)
