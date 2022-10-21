# 1092 - 배

import sys
input = sys.stdin.readline

n = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
else:
    answer = 0
    while True:
        if len(boxes) == 0:
            break
        answer += 1
        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
    print(answer)