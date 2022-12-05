# 2457 - 공주님의 정원

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    a, b, c, d = map(int, input().split())
    if 100*c+d < 301 or 100*a+b > 1130: continue 
    arr.append([100*a+b, 100*c+d])  