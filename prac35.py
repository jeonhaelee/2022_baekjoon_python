# 17404 - RGB거리_2

import sys
input = sys.stdin.readline

n = int(input())
house = []
for _ in range(n):
    house.append(list(map(int, input().split())))
    
answer = 1e9
for i in range(3):
    dp = [[1e9, 1e9, 1e9] for _ in range(n)]
    dp[0][i] = house[0][i]
    for j in range(1, n):
        dp[j][0] = house[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = house[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = house[j][2] + min(dp[j-1][0], dp[j-1][1])
    for c in range(3):
        if i != c:
            answer = min(answer, dp[-1][c])
            
print(answer)
