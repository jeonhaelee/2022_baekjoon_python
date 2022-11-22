# 1065 - 한수

import sys

num = int(input())

def check(number):
    numbers = list(str(number))
    d = int(numbers[1]) - int(numbers[0])
    
    for i in range(2, len(numbers)):
        if int(numbers[i]) - int(numbers[i-1]) != d:
            return False
        
    return True
            
answer = 0
for n in range(1, num+1):
    if n < 10:
        answer += 1
    else:
        if check(n):
            answer += 1
        
print(answer)
