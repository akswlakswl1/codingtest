#계수 정렬 : 크기가 한정되어 있고 데이터의 크기가 많이 중복되어 있을 때 유라
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(array) + 1) #마지막 숫자까지 적용하기위해 +1

for i in range(len(array)):
    count[array[i]] +=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')