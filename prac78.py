# 8983 - 사냥꾼

from bisect import bisect_left
import sys
input = sys.stdin.readline

m, n, l = map(int, input().split()) # 사대의 수, 동물의 수, 사정거리
hunter = list(map(int, input().split())) # 사대 위치 리스트
hunter.sort()

animal = [] # 동물 위치 리스트
for _ in range(n):
    x, y = map(int, input().split())
    if y > l: # y가 사정거리보다 크면 애초에 불가능하니까 continue
        continue
    else:
        animal.append([x, y])

def fine_hunter(hunter, v):
    idx = bisect_left(hunter, v) # 사대 위치 리스트에서 v가 들어갈 위치 인덱스
    if idx == 0:
        return hunter[0] # idx가 0이면 제일 가까운 사대의 위치는 hunter[0]
    if idx == len(hunter):
        return hunter[-1] # idx가 len(hunter) - 1 이면 제일 가까운 사대의 위치는 hunter[-1]
    if hunter[idx] - v < v - hunter[idx-1]: # 주변 사대 위치 중 더 가까운 사대 위치를 리턴
        return hunter[idx]
    return hunter[idx-1]
        
answer = 0
for x, y in animal:
    idx = fine_hunter(hunter, x)
    if abs(idx - x) + y > l: # 동물의 x좌표와 사대 위치와의 거리와, y를 더한 값이 사정거리보다 크면 continue
        continue
    else:
        answer += 1
        
print(answer)