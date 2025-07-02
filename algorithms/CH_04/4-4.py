#게임 개발

#세로,가로 크기 받아오기
n,m = map(int,input().split())

#맴 초기화
d = [[0] * m  for _ in range(n)]

#현재 위치, 방향 입력
x,y,dir = map(int,input().split())
d[x][y] = 1
count = 1

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

#북 동 남 서
dx = [-1,0,1,0] #y방향
dy = [0,1,0,-1] #x방향

#왼쪽으로 회전
def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir  = 3

#처음은 항상 육지
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

        if turn_time == 4:
            nx = x - dx[dir]
            ny = y - dy[dir]
            
            if array[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0

print(count)
