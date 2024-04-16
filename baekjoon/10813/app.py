# 파이썬 초기화 컴프리헨션 arr = [i for i in range(1,n+1)]

n,m = map(int,input().split())

arr = [i for i in range(1,n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    an = arr[a-1]
    bn = arr[b-1]
    arr[a-1] = bn
    arr[b-1] = an

print(*arr)
