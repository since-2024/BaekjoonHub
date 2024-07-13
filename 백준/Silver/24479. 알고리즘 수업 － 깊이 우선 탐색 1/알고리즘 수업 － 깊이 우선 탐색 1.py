import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)


def dfs(t):
    global cnt
    visited[t] = cnt
    graph[t].sort()
    for i in graph[t]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
cnt = 1

dfs(r)

for i in range(1, n+1):
    print(visited[i])