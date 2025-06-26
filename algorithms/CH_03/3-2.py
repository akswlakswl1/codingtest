#1. 숫자 입력 받기 n,m,k
n,m,k = map(int,input().split())
#2. n개의 수 입력 받기 =
numbers = list(map(int,input().split()))
numbers.sort()
#3. 큰수 작은수 입력 받기
first = numbers[n-1]
second = numbers[n-2]

#4. m만큼 반복하는데 같은 수를 k 만큼 더할 수 있음
cnt = 0
sum = 0
for _ in range(m):
    if cnt != k:
        sum = sum + first
        cnt = cnt + 1
    else:
        cnt = 0
        sum = sum + second

    #첫번째 수를 k 만큼 더함
    #두번쨰 한번 더함 
    #다시 첫번쨰 수를 K 만큼 더함

# print(sum)

#반복되는 수열을 구해서 계산할 수도 있음 - 첫번째수 k + 두번째수 => k+1
#5 8 3일경우 8번 더하는데 3번반복가능함
# count = (8 / (3 + 1)) * k  반복되는 수열 * 반복가능한 첫번쨰수
# count += m % (k+1) 나누어 떨어지지 않았을 시 첫번째수 더하기
count = int(m/ (k+1))* k 
count += m % (k+1)
sum = (first * count) + (second * (m-count))
print(sum)