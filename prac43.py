# 1929 - 소수
# 에라토스테네스의 체 문제
# -> 해당 수의 제곱근을 구해 그 제곱근까지의 약수만 확인해주면 나머지 수도 판단할 수 있다.

import sys
input = sys.stdin.readline

m, n = map(int, input().split())
    
for i in range(m, n+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else: print(i)