# 11000 - 강의실 배정
# 시간초과

n = int(input())

start_time = []
end_time = []

cnt = 0
while cnt < n:
    s, e = map(int, input().split())
    if s in end_time:
        idx = end_time.index(s)
        end_time[idx] = e
    else:
        start_time.append(s)
        end_time.append(e)
    cnt += 1
        
print(len(start_time))