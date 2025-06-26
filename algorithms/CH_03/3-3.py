#숫자 카드 게임


#1. n,m받아오기
n,m = map(int,input().split())
array = []
#2. 각 행마다 숫자 입력 받기
for _ in range(n):
    row = list(map(int,input().split()))
    #3. 각 행마다 가장 작은수 저장
    min_value = min(row)
    array.append(min)
#4. 그 중 큰 수 출력
print(max(array))

#array에 담아두지 않고 끝날때마다 비교하여 저장할 수도 있음
n,m = map(int,input().split())
result = 0
#2. 각 행마다 숫자 입력 받기
for _ in range(n):
    row = list(map(int,input().split()))
    #3. 각 행마다 가장 작은수 저장
    min_value = min(row)
    result = max(result,min_value)
#4. 그 중 큰 수 출력
print(result)