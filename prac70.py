# 11650 - 좌표 정렬하기

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]

li.sort(key=lambda x: (x[0], x[1]))

for l in li:
    print(*l)