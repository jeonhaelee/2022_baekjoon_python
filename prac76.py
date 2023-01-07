# 1477 - 휴게소 세우기

import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
rest_area = [0] + list(map(int, input().split())) + [l]
rest_area.sort()

# 휴게소 사이의 거리
dist = []
for i in range(1, len(rest_area)):
    dist.append(rest_area[i] - rest_area[i-1])

start = 1
end = l - 1

answer = 0
while start <= end:
    mid = (start + end) // 2
    
    count = 0
    for d in dist:
        if d > mid:
            count += (d - 1) // mid
            # - 1 을 해주는 이유 : 'd == mid' 일 경우 때문에
        
    if count > m:
        start = mid + 1
    
    else:
        answer = mid
        end = mid - 1
        
print(answer)

