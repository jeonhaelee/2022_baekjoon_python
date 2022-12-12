# 1931 - 회의실 배정

import sys
input = sys.stdin.readline

n = int(input())
lec_li = [list(map(int, input().split())) for _ in range(n)]

lec_li.sort(key=lambda x:(x[1], x[0]))

answer = 1
end = lec_li[0][1]

for li in lec_li[1:]:
    if li[0] >= end:
        end = li[1]
        answer += 1
        
print(answer)
