# 1753 - 최단경로

import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
node = {}

# node 딕셔너리에 출발점을 key로 해서 넣어주기
for _ in range(e):
    start, end, value = map(int, input().split())
    try:
        node[start].append([end, value])
    except:
        node[start] = [[end, value]]
        
q = []
dis = [1e9 for _ in range(v+1)]
dis[k] = 0

heapq.heappush(q, (0,k))

while q:
    cur_dis, cur = heapq.heappop(q)
    
    if cur not in node.keys():
        continue
    
    for nex, nex_dis in node[cur]:
        nex_dis += cur_dis
        if dis[nex] > nex_dis:
            dis[nex] = nex_dis
            heapq.heappush(q, (nex_dis, nex))

for d in dis[1:]:
    if d == 1e9:
        print("INF")
    else:
        print(d)