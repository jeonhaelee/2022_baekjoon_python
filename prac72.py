# 3273 - 두 수의 합

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

a, b = 0, len(arr)-1
answer = 0
while a < b:
    if arr[a] + arr[b] == x:
        answer += 1
        a += 1
        b -= 1
    elif arr[a] + arr[b] > x:
        b -= 1
    elif arr[a] + arr[b] < x:
        a += 1

    
print(answer)