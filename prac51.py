# 2839 - 설탕배달

import sys

num = int(input())

# 5로 나누어 떨어질 때
if num % 5 == 0:
    print(num // 5)
    sys.exit()
    
# 5로 나누어 떨어지고, 3으로 나누어 떨어질 때
answer = 0
while True:
    answer += num // 5
    remain = num % 5
    if remain % 3 != 0:
        answer = 0
        break
    answer += remain // 3
    break

if answer > 0:
    print(answer)
    sys.exit()
    
# 3으로 나누어 떨어질 때
if num % 3 == 0:
    print(num // 3)
    sys.exit()
    
# 그 외
print(-1)
