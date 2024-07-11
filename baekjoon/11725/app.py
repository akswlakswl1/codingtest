import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, v,parent):
    for i in graph[v]:
        if parent[i] == 0:
            parent[i] = v
            dfs(graph,i,parent)

n = int(input())
graph = [[] for i in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n+1)

dfs(graph,1,parent)

for i in range(2, n+1):
    print(parent[i])
