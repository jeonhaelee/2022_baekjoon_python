# 1339 - 단어 수학

import sys
input = sys.stdin.readline

N = int(input())
str_list = []
dic = {}
count_dic = {}
for _ in range(N):
    string = list(input())[:-1]
    str_list.append(string)
    for i, s in enumerate(string):
        if s in count_dic:
            count_dic[s] += 1
        else:
            count_dic[s] = 1
        if s in dic and dic[s] < (len(string) - i):
            dic[s] = len(string) - i
        elif s not in dic:
            dic[s] = len(string) - i

dic2 = {}
for k, v in dic.items():
    if v in dic2:
        dic2[v].append(k)
    else:
        dic2[v] = [k]

dic2 = dict(sorted(dic2.items(), key = lambda x:x[0], reverse=True))

dic_li = []
for v, k in dic2.items():
    li = sorted(k, key =lambda x:count_dic[x], reverse=True)
    dic_li.extend(li)
    
number_dic = {}
l = 9
for s in dic_li:
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