# 16398 - 행성 연결

from heapq import heappop, heappush

import sys
input = sys.stdin.readline

def union(node1, node2): # 부모 노드를 합쳐주는 함수
    global parents

    P1 = Find(node1)
    P2 = Find(node2)
    
    parents[P2] = P1
    return

def Find(node): # 부모 노드를 찾아주는 함수
    global parents

    if parents[node] == node:
        return node
    
    else :
        P = Find(parents[node])
        parents[node] = P
        return P


n = int(input())
parents = [i for i in range(n)] # 부모노드를 저장할 변수
# 초기값은 본인 자신의 노드 번호
            
edge = []

for i in range(n):
    info = list(map(int, input().split()))
    for j, node in enumerate(info):
        if node != 0:
            heappush(edge, (node, i, j)) # edge에 (관리비용, 노드i, 노드j)를 넣어줌
        
ans = 0
connected_edge = 0 # 연결된 edge 개수
while connected_edge != n - 1: # connected_edge가 n-1이 되면 종료
    edge_distance, node1, node2 = heappop(edge) # 현재 edge에서 관리비용이 제일 적은 노드 Set을 꺼냄
    if Find(node1) != Find(node2): # 부모노드가 같다면 pass, 같지 않다면
        union(node1,node2) # 두 노드를 연결해주고
        ans += edge_distance # ans에 두 노드를 연결하는데 쓰이는 관리비용을 더해줌
        connected_edge += 1 # 연결된 edge에 +1 해줌

print(ans)
