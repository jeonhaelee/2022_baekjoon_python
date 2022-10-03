# 1744 - 수 묶기

N = int(input())
arr = [int(input()) for _ in range(N)]

positive = []
negative = []

answer = 0

for n in arr:
    if n == 1:
        answer += 1
    elif n <= 0:
        negative.append(n)
    else:
        positive.append(n)

negative.sort()
positive.sort(reverse=True)

if len(negative) % 2 != 0:
    negative.append(1)
if len(positive) % 2 != 0:
    positive.append(1)

for i in range(0, len(negative), 2):
    answer += (negative[i] * negative[i+1])
for i in range(0, len(positive), 2):
    answer += (positive[i] * positive[i+1])

print(answer)

# input : 4 -1 2 1 3 
# output : 6
