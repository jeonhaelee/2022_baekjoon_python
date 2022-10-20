# 10773 - 제로

k = int(input())
answer = []
for _ in range(k):
    num = int(input())
    if num == 0:
        del answer[-1]
    else:
        answer.append(num)
print(sum(answer))