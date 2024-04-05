#파이썬에서 int 값 중 가장 큰 값을 구할 때 max() 함수를 활용하면 된다

a,b,c = map(int,input().split())

if a == b == c:
  print(10000+(a*1000))
elif a == b or a == c:
  print(1000+(a*100))
elif b == c:
  print(1000+(b*100))
else:
  print(max(a,b,c)*100)
