# 5014 - 스타트링크


from collections import deque

f, s, g, u, d = map(int, input().split())


floor_cnt = [1e9]*(f+1)
visited = [0]*(f+1)
visited[s] = 1
floor_cnt[s] = 0


q = deque()
q.append((s, 0))
while q:
    now, cnt = q.popleft()
    if now == g:
        break
    
    for i in [u, -d]:
        next = now + i
        if next > 0 and next <= f and not visited[next]:
            visited[next] = 1
            floor_cnt[next] = cnt + 1
            q.append((next, floor_cnt[next]))
    
    
ans = floor_cnt[g]
if ans == 1e9:
    print("use the stairs")
else:
    print(ans)