# 1202 - 보석 도둑


import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
j_list = [list(map(int, input().split())) for _ in range(n)]
b_list = [int(input()) for _ in range(k)]

j_list.sort()
b_list.sort()

answer = 0
tmp = []

for bag in b_list:
    while j_list and j_list[0][0] <= bag:
        heapq.heappush(tmp, -j_list[0][1])
        heapq.heappop(j_list)
    if tmp:
        answer -= heapq.heappop(tmp)
        
print(answer)