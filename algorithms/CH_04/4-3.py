#왕실의 나이트


#8*8크기의 체스판이 있음
count = 0

#상,하로 두칸씩 이동 한 후 좌,우로 이동이 가능한지
#좌,우로 두칸씩 이동 한 후 상.하로 이동이 가능한지
types = ['a','b','c','d','e','f','g','h']

#1. 현재 위치 받아오기
pos = str(input())
#a,b,c 앞의 좌표도 숫자로 변경해야함
x = int(types.index(pos[0])) + 1
y = int(pos[1])

dx = [0,0,-2,2]
dy = [-2,2,0,0]

#상
if y - 2 >= 1:
    #좌우 확인
    nx = x + dx[0]
    ny = y + dy[0]
    if nx + 1 <= 8:
        count += 1
    if nx -1 >= 1:
        count += 1
#하
if y + 2 <= 8:
    #좌우 확인
    nx = x + dx[1]
    ny = y + dy[1]
    if nx + 1 <= 8:
        count += 1
    if nx -1 >= 1:
        count += 1
#좌
if x - 2 >= 1:
    #상하 확인
    nx = x + dx[2]
    ny = y + dy[2]
    if ny + 1 <= 8:
        count += 1
    if ny -1 >= 1:
        count += 1
#우
if x + 2 <= 8:
    #상하 확인
    nx = x + dx[3]
    ny = y + dy[3]
    if ny + 1 <= 8:
        count += 1
    if ny -1 >= 1:
        count += 1

#print(count)

#여기서 중복적인 부분들이 많고 복잡함. 생각을 좀 더 해보면 현재 위치에서 
#이동할 수 있는 모든 경로는 최대 8가지이기 때문에 이걸 비교해 보면됨
steps = [[-2,1],[-2,-1],[2,1],[2,-1],[1,-2],[-1,-2],[1,2],[-1,2]]
x = int(types.index(pos[0])) + 1
y = int(pos[1])
result = 0

for pos in steps:
    nx = x + pos[0]
    ny = y + pos[1]
    if nx >= 1 and nx <= 8 and ny >=1 and ny <= 8:
        result += 1
print(result)



