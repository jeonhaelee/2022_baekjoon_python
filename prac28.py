# 9625 - BABBA

k = int(input())

count_a = 1
count_b = 0

for _ in range(k):
    count_a, count_b = count_b, count_a + count_b
    
print(count_a, count_b)