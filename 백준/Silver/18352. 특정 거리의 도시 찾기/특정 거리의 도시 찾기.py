from collections import deque
import sys
input = sys.stdin.readline


n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque([x])
dist = [-1] * (n+1)
dist[x] = 0
ans = []

while q:
    node = q.popleft()
    for i in graph[node]:
        if dist[i] < 0:
            q.append(i)
            dist[i] = dist[node] + 1
            if dist[i] == k:
                ans.append(i)

if ans:
    ans.sort()
    for i in ans:
        print(i)
else:
    print(-1)