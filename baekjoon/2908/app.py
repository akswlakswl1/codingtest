#str을 반대로 변경 a[::-1]


a,b = map(str,input().split())
a = int(a[::-1])
b = int(b[::-1])
print(max(a,b))
