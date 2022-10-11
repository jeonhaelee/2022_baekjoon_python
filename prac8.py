# 21608 - 상어초등학교


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N*N)]
info = [[[-1, -1, i, j] for j in range(N)] for i in range(N)]
seat = [[0 for j in range(N)] for i in range(N)]

def check_adjacent(i, j, student):
    global N
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    like_count = 0
    empty_count = 0
    
    for k in range(4):
        if 0 <= i + di[k] < N and 0 <= j + dj[k] < N:
            if seat[i+di[k]][j+dj[k]] in student[1:]:
                like_count += 1
            elif seat[i+di[k]][j+dj[k]] == 0:
                empty_count += 1
                
    return [like_count, empty_count, i , j]


for student in arr:
    for i in range(N):
        for j in range(N):
            info[i][j] = [-1, -1, i, j]
            if seat[i][j] == 0:
                info[i][j] = check_adjacent(i, j, student)
    one_d_info = sum(info, [])
    one_d_info.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    seat[one_d_info[0][2]][one_d_info[0][3]] = student[0]

            
like_dict = dict()
for student in arr:
    like_dict[student[0]] = student[1:]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

answer = 0
for i in range(N):
    for j in range(N):
        like = like_dict[seat[i][j]]
        neighbor = []
        for k in range(4):
            if 0 <= i+di[k] < N and 0 <= j+dj[k] < N: 
                neighbor.append(seat[i+di[k]][j+dj[k]])
        near_like_cnt = len(set(neighbor) & set(like))
        answer += 10 ** (near_like_cnt-1) if near_like_cnt > 0 else 0
        
print(answer)
