#1이 될때까지

#1. 두 수를 입력 받는다
n,k = map(int,input().split())

#나눌수 있으면 나누고 아니면 1을 뺀다.
count = 0
while True:
    if n == 1:
        break

    if n % k == 0:
        n = n / k
    else:
        n -= 1
    count += 1

print(count)
