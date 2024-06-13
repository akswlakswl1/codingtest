# 모든 가능한 순열 생성
permutations = itertools.permutations(data)

import itertools
n = int(input())
data = list(map(int,input().split()))
A = itertools.permutations(data)
max = []
for lst in A:
    sum = 0
    for i in range(len(lst)-1):
        sum += abs(lst[i] - lst[i+1])
    max.append(sum)
max.sort()
print(max[len(max)-1])
