# 11000 - 강의실 배정


import heapq
import sys

n = int(input())

time_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

time_list.sort()

end_time_queue = []
heapq.heappush(end_time_queue, time_list[0][1])

for i in range(1, n):
    if time_list[i][0] < end_time_queue[0]:
        heapq.heappush(end_time_queue, time_list[i][1])
    else:
        heapq.heappop(end_time_queue)
        heapq.heappush(end_time_queue, time_list[i][1])

print(len(end_time_queue))
