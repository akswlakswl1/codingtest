n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

#k번 바꿔치기
#a는 으로 하고 b는 내림차순으로해서 바꾸면 되지않나?
a.sort()
b.sort(reverse=True)

for i in range(k):
    a[i] = b[i]

print(sum(a))