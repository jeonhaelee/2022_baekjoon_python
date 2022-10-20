# 11399 - ATM

N = int(input())
people = list(map(int, input().split()))
people.sort()
sum = 0
sub_sum = 0
for time in people:
    sub_sum = (sub_sum + time)
    sum += sub_sum
print(sum)
