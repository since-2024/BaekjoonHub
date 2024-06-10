from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[False] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visitedD = [False] * (n+1)
visitedB = [False] * (n+1)


# DFS
def dfs(v):
    visitedD[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if not visitedD[i] and graph[v][i]:
            dfs(i)


# BFS
def bfs(v):
    q = deque([v])
    visitedB[v] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if not visitedB[i] and graph[v][i]:
                q.append(i)
                visitedB[i] = True


dfs(v)
print()
bfs(v)