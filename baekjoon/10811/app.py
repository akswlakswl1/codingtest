#리스트 특정 범위 가져오기 , reverse

n,m = map(int,input().split())

arr = list(range(1,n+1))

for _ in range(m):
    i,j = map(int,input().split())
    arr[i-1:j] = reversed(arr[i-1:j])  

print(*arr)
