#배열 공백으로 출력하고 싶으면 print(*arr) 사용

b, n = map(int, input().split())

arr = [0] *b

for _ in range(n):
    i,j,k = map(int, input().split())
    for l in range(i-1,j):
        arr[l] = k

print(*arr) 
