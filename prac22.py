# 1946 - 신입 사원


import sys
input = sys.stdin.readline

n = int(input())

while n > 0:
    people = []
    p_n = int(input())
    for _ in range(p_n):
        a, b = map(int, input().split())
        people.append([a, b])
    people_sorted = sorted(people)
    hired = 1
    val = people_sorted[0][1]
    for i in range(1, p_n):
        if people_sorted[i][1] < val:
            val = people_sorted[i][1]
            hired += 1
    print(hired)
    n -= 1
