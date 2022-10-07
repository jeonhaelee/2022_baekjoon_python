# 14719 - 빗물

H, W = map(int, input().split()) # 사실 풀이에선 얘 없어도 됨
blocks = list(map(int, input().split()))

answer = 0

for i in range(1, len(blocks)-1):
    max_l = max(blocks[:i])
    max_r = max(blocks[i+1:])
    
    max_min = min(max_l, max_r)

    if blocks[i] < max_min:
        answer += max_min - blocks[i]
        
print(answer)