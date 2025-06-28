#상하좌우

#1. 데이터 입력받기
n = int(input())
datas = list(input().split())

#2. n*n 배열생성
# L은 -1,0 R은 1,0 ,U는 0,1, D는 0,-1
current = [1,1]
for i in datas:
    if i == 'L' and current[1] >1:
        current[1] -= 1
    elif i == 'R' and current[1] < n:
        current[1] += 1
    elif i == 'U' and current[0] > 1:
        current[0] -= 1
    elif i == 'D' and current[0] < n:
        current[0] += 1

    #print(current)
#4.결과 출력
#print("최종  ",current)

#공간에서 이동하는 문제는 매핑 테이블을 만들어서 사용하면 유용함
x = 1
y = 1

dx = [0,0,-1,1] #행이동 -> 상하
dy = [-1,1,0,0] #열이동 -> 좌우
types = ['L','R','U','D']

for data in datas:
    for i in range(len(types)):
        if data == types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx,ny

print(x,y)