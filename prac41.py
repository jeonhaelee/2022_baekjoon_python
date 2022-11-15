# 16953 - A -> B

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

count = 1

# b에서 a로 만들어주기
while True:
    if b == a:
        break
    elif (b % 2 != 0 and b % 10 != 1) or (b < a): # a로 만들어 줄 수 없는 경우
        count = -1
        break
    else:
        if b % 10 == 1: # 연산의 횟수를 줄이기 위해선 2를 곱하는 것보다 끝에 1을 붙이는 것이 더 좋다.
            b //= 10
            count += 1
        elif b % 2 == 0:
            b //= 2
            count += 1
            
print(count)