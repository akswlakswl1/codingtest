# History
# 처음에는 단순히 이중 for문을 돌려서 값을 계산하려고 했음
# 그러다가 더 효율적인 방법이 있을 것 같았다
#
# 문제를 봤을 때 단순히 print만 하면되서 B의 자리수 마다 하나씩 곱하면 되었음
# 마지막 두 수를 곱하는 계산식은 그냥 바로 곱하면 되었음
#
# 너무 복잡하게 생각하지말고 규칙을 찾는 것에 집중하자


A = int(input())
B = input()

first = A*int(B[2])
second = A*int(B[1])
third = A*int(B[0])

print(first)
print(second)
print(third)
print(A*int(B))
