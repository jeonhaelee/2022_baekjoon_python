# 2224 - 명제 증명

import sys
input = sys.stdin.readline

n = int(input())
check = [[0] * 58 for _ in range(58)]

count = 0
for _ in range(n):
    sentence = input()
    before, after = ord(sentence[0])-65, ord(sentence[5])-65
    if before == after or check[before][after]:
        continue
    check[before][after] = 1
    count += 1
    
for k in range(58):
    for i in range(58):
        for j in range(58):
            if i != j and check[i][k] == 1 and check[k][j] == 1 and not check[i][j]:
                check[i][j] = 1
                count += 1
            
print(count)    
for i in range(58):
    for j in range(58):
        if check[i][j] == 1:
            print(chr(i+65), "=>", chr(j+65))