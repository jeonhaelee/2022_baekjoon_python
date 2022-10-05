# 2108 - 통계학

import sys
from collections import Counter


N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]


answer1 = round(sum(arr)/N)
arr.sort()
answer2 = arr[N//2]
answer4 = max(arr) - min(arr)


cnt = Counter(arr).most_common()
answer3 = cnt[0][0]
if N != 1:
    if cnt[0][1] == cnt[1][1]:
        answer3 = cnt[1][0]


print("--------------------")


print(answer1)
print(answer2)
print(answer3)
print(answer4)

# 5
# 1
# 3
# 8
# -2
# 2

# 2
# 2
# 1
# 10