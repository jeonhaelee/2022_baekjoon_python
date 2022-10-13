# 1388 - 바닥 장식


# 내 풀이

N, M = map(int, input().split())

floor = []
for _ in range(N):
    floor.append(list(input()))
    
answer = 0

for i in range(N):
    if floor[i][0] == "-":
        answer += 1
    for j in range(1, M):
        if floor[i][j] == "-":
            if floor[i][j] != floor[i][j-1]:
                answer += 1
                
for j in range(M):
    if floor[0][j] == "|":
        answer += 1
    for i in range(1, N):
        if floor[i][j] == "|":
            if floor[i][j] != floor[i-1][j]:
                answer += 1
                
print(answer)


# 다른 사람 풀이

N, M = map(int, input().split())

floor = []
for _ in range(N):
    floor.append(list(input()))
    
answer = 0

for i in range(N):
    pre = "/"
    for j in range(M):
        if floor[i][j] == "-":
            if floor[i][j] != pre:
                answer += 1
        pre = floor[i][j]
        
for j in range(M):
    pre = "/"
    for i in range(N):
        if floor[i][j] == "|":
            if floor[i][j] != pre:
                answer += 1
        pre = floor[i][j]
        
print(answer)

