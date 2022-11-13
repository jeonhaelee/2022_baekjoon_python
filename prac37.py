# 1300 - K번째 수

n = int(input())
k = int(input())

def num_count(num):
    cnt = 0
    for i in range(1, n + 1):
        if num // i > 0:
            cnt += min(n, num // i)
        else:
            break
    return cnt

def bs(start, end, k):
    mid = (start + end) // 2
    if start == mid:
        if num_count(start) == k:
            return start
        else:
            return start + 1
        
    cnt = num_count(mid)
    
    if cnt >= k:
        return bs(start, mid, k)
    
    elif cnt < k:
        return bs(mid, end, k)
    
print(bs(1, n**2, k))