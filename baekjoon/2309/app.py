#문제를 접근할 적에 선언을 하고 그 뒤에 함수를 활용하여 과정을 도출

def solve():
    N = 9
    num = sum(lst) - 100
    for i in range(N-1):
        for j in range(i+1,N):
            if lst[i] + lst[j] == num:
                return lst[i], lst[j]

lst = [int(input()) for _ in range(9)]
n,m = solve()
for i in sorted(lst):
    if i != n and i != m:
        print(i)
