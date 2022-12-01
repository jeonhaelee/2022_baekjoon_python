# 1339 - 단어 수학

import sys
input = sys.stdin.readline

N = int(input())
str_list = []
dic = {} 
for _ in range(N):
    string = list(input())[:-1]
    str_list.append(string)
    for i, s in enumerate(string):
        if s in dic and dic[s] < (len(string) - i):
            dic[s] = len(string) - i
        elif s not in dic:
            dic[s] = len(string) - i

dic = dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))

number_dic = {}
l = 9
for s in dic:
    number_dic[s] = l
    l -= 1

def change_num(s):
    return str(number_dic[s])

answer = 0
for string in str_list:
    number = ''
    for s in string:
        s = change_num(s)
        number += s
    answer += int(number)
    
print(answer)