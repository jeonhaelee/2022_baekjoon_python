# 5052 - 전화번호 목록
# pypy로 제출하면 통과!

import sys
input = sys.stdin.readline

def check_number(call_nums):
    for i in range(len(call_nums)):
        for j in range(i+1, len(call_nums)):
            if call_nums[j].startswith(call_nums[i]):
                return 'NO'
    return 'YES'
    
t = int(input())
for _ in range(t):
    n =  int(input())
    call_nums = [input()[:-1] for _ in range(n)]
    call_nums.sort(key=lambda x:len(x))
    print(check_number(call_nums))
    
