# 2581 - 소수


import math

m = int(input())
n = int(input())

def check(num):
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True

True_li = []
for number in range(m, n+1):
    if number == 1:
        continue
    if check(number):
        True_li.append(number)
        
if len(True_li) == 0:
    print(-1)
else:
    print(sum(True_li))
    print(min(True_li))