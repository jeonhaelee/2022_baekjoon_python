# 1507 - 궁금한 민호

import sys
input = sys.stdin.readline

n = int(input())
citymap = []
check = [[1] * n for _ in range(n)]
answer = 0

for _ in range(n):
    citymap.append(list(map(int, input().split())))
    
for k in range(n): # 사이에 있는 도시
    for i in range(n): # 시작 도시
        for j in range(n): # 끝 도시
            if i == j or j == k or i == k: # '시작 도시 = 끝 도시일 경우'와 '사이에 있는 도시가 시작 도시나 끝 도시일 경우'는 제외해줌
                continue
            if citymap[i][j] == citymap[i][k] + citymap[k][j]: # 사이에 있는 도시를 통해 최단거리로 갈 수 있다면 시작 도시와 끝 도시를 잇는 도로는 없애줌
                check[i][j] = 0
            elif citymap[i][j] > citymap[i][k] + citymap[k][j]: # 불가능한 경우이므로 answer를 -1로 바꿔줌
                answer = -1
                
if answer != -1:
    for i in range(n): 
        for j in range(i, n): # 양방향 도로이니 반만 해주기 위해 i부터 n까지만!
            if check[i][j] == 1: # 해당 도로의 check 값이 1이면
                answer += citymap[i][j] # 해당 도로의 가중치를 answer에 더해줌

print(answer)