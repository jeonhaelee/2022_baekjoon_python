# 11054 - 가장 긴 바이토닉 부분 수열

from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input()) 
arr = [*map(int,input().split())] 

def getlis(arr): 
    
    dp=[];lis=[] 
    for num in arr:
        idx = bisect_left(dp,num)
        lis+=[idx+1]
        
        if len(dp)==idx:
            dp+=[num]
        else:
            dp[idx]=num
            
    return lis

lis = getlis(arr)
lds = getlis(arr[::-1])[::-1]

print(max(i+d-1 for i,d in zip(lis,lds)))