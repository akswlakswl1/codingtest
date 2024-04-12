# 단순히 반복만 하고 싶을 때는 _를 사용해준다.
# print ,end=(' ')를 사용하면 띄워쓰기를 해준다.

num = int(input())
list = num//4

for _ in range(list):
    print('long',end=(' '))
    
print('int', end=(' '))
