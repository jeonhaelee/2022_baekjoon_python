#1181 - 단어 정렬

n = int(input())
li = []
for _ in range(n):
    w = input()
    if [len(w),w] not in li:
       li.append([len(w),w])
li.sort()
for l, w in li:
    print(w)
