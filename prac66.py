# 2212 - 센서

import sys
input = sys.stdin.readline

n = int(input()) # 센서의 개수
k = int(input()) # 집중국의 개수
censor = list(map(int, input().split())) # 센서
censor.sort() # 오름차순으로 센서 정렬

# k >= n 이면, 모든 센서의 위치에 집중국이 위치할 수 있으므로 수신가능거리가 0이 됨
if k >= n: 
    print(0)
    sys.exit()
    
dist = [] # 센서 간 거리를 담을 리스트
for c in range(len(censor)-1):
    d = censor[c+1] - censor[c] 
    dist.append(d)

# 사이의 거리가 먼 센서들을 먼저 나눠주기 위해 내림차순으로 정렬
dist.sort(reverse=True) 

# K개의 그룹으로 만들기 위해 K-1번 잘라줌 => 사이의 거리가 먼 센서 거리부터 K-1번 없애줌
for _ in range(k-1):
    dist.pop(0)

# 그룹으로 나눠진 센서들의 사이 거리의 합을 구해주면 됨 => dist 나머지의 합을 구해주는 것
answer = sum(dist)
print(answer)