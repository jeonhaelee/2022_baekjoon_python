# 1339 - 단어 수학

import sys
input = sys.stdin.readline

N = int(input()) # 단어 개수 입력받기

words = [] # 단어 입력 받아서 넣을 리스트
for _ in range(N): # N개의 단어 입력 받기
    words.append(list(input().rstrip()))

alpha_dic = {} # 각각의 알파벳이 어느 자리수에 있는지 판단할 수 있는 딕셔너리
for word in words: # 입력 받은 단어 돌면서
    l = len(word) # 해당 단어의 길이
    for i in range(l): # 단어의 알파벳 하나하나 자리수를 확인해준다
        if word[i] not in alpha_dic: # 
            alpha_dic[word[i]] = 10 ** (l - 1 - i) # 예) AB의 A일 때, 10 ** (2 - 1 - 0) = 10
        else:
            alpha_dic[word[i]] += 10 ** (l - 1 - i) # 더해주기 때문에 알파벳 개수까지 파악가능

# 알파벳에 숫자를 지정해주기 위해, value 값을 기준으로 내림차순 정렬해준다
alpha_dic = sorted(alpha_dic.items(), key=lambda x: x[1], reverse=True)

alpha_to_num = {} # 알파벳과 숫자 짝지어서 넣어주는 딕셔너리
num = 9 # 숫자 범위는 0 ~ 9
for alpha in alpha_dic: # 위에서 정렬해준 순서대로(가장 큰 값을 갖는 알파벳) 9부터 넣어준다
    alpha_to_num[alpha[0]] = num
    num -= 1

answer = 0
for word in words: # 입력받은 단어들 돌면서
    num = ""
    for alpha in word: # 각 단어의 알파벳을 숫자로 바꿔주고
        num += str(alpha_to_num[alpha])
    
    answer += int(num) # answer에 더해준다

print(answer)