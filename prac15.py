# 11000 - 강의실 배정
# 시간초과2

import time
start = time.time()

n = int(input())

time_dic = {}

cnt = 0
while cnt < n:
    s, e = map(int, input().split())
    if s in time_dic.values():
        for key, value in time_dic.items():
            if value == s:
                time_dic[key] = e
                break
    else: time_dic[s] = e
    cnt += 1

    
print(len(time_dic))
print(f'time : {time.time() - start}')