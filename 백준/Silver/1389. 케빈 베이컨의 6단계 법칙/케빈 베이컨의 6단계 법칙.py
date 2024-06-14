from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

res = []

for i in range(1, n+1):
    q = deque([i])
    num = [0] * (n+1)
    visited = [i]

    while q:
        v = q.popleft()

        for j in graph[v]:
            if j not in visited:
                q.append(j)
                visited.append(j)
                num[j] = num[v] + 1

    res.append(sum(num))

print(res.index(min(res)) + 1)