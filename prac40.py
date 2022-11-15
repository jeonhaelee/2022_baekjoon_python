# 2143 - 두 배열의 합

from collections import Counter
import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
a_arr = list(map(int, input().split()))
m = int(input())
b_arr = list(map(int, input().split()))

answer = 0
c = Counter()

for s in range(n):
    for e in range(s, n):
        c[sum(a_arr[s:e+1])] += 1
        
for s in range(m):
    for e in range(s, m):
        num = t - sum(b_arr[s:e+1])
        answer += c[num]
        
print(answer)