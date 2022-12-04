# 10800 - 컬러볼

import sys
input = sys.stdin.readline

N = int(input())
balls = []
answer = [0]*N
color_sum = {}
size_sum = {}
color_size_sum = {}
for i in range(N):
    a,b = map(int,input().split())
    color_sum[a] = 0      
    size_sum[b] = 0       
    color_size_sum[(a,b)] = 0
    balls.append([i,a,b]) 

balls.sort(key= lambda x: (x[2], x[1]))
until_now_sum = 0  

for ball in balls:
    num, col, siz = ball
    answer[num] += until_now_sum - color_sum[col] - size_sum[siz] + color_size_sum[(col,siz)]
    until_now_sum += siz
    color_sum[col] += siz
    size_sum[siz] += siz
    color_size_sum[(col,siz)] += siz
    
for i in answer:
    print(i)