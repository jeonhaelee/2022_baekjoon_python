# 1931 - 회의실 배정

import sys
input = sys.stdin.readline

n = int(input())
lec_li = [list(map(int, input().split())) for _ in range(n)]

lec_li.sort()

answer = 0
start = 0; end = lec_li[0][1]

for li in lec_li:
    if li[0] >= end:
        start = li[0]
        end = li[1]
        answer += 1
        
print(answer)