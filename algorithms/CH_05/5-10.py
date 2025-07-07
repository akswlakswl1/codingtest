n,m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    #예외 처리
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        #상하좌우 탐색
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        #새로운 영역을 처음 탐색 시작했을 때만 True
        return True 
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result +=1

print(result)

