# 1309 - 동물원

n = int(input())
cage = [[0, 0, 0] for _ in range(n)]
cage[0] = [1, 1, 1]

for i in range(1, n):
    cage[i][0] = (cage[i-1][0] + cage[i-1][1] + cage[i-1][2]) % 9901
    cage[i][1] = (cage[i-1][0] + cage[i-1][2]) % 9901
    cage[i][2] = (cage[i-1][0] + cage[i-1][1]) % 9901
    
print(sum(cage[-1]) % 9901)