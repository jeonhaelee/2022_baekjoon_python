# 20300 - 서강근육맨

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

max_val = 0
if len(arr) % 2 != 0:
    max_val = arr.pop()

while arr:
    sum = arr.pop(0) + arr.pop()
    max_val = max(max_val, sum)

print(max_val)



# 5
# 1 2 3 4 5

# 5