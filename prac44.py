# 1197 - 최소 스패닝 트리

import sys
input = sys.stdin.readline

v, e = map(int, input().split())
trees = [list(map(int, input().split())) for _ in range(e)]
parent = list(range(v+1))
trees.sort(key=lambda x:x[2])

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

result = 0
for a, b, c in trees:
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        if a_root > b_root:
            parent[a_root] = b_root
        else:
            parent[b_root] = a_root
        result += c
print(result)