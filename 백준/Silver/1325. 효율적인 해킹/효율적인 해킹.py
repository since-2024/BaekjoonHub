from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = []
ans_max = 0

for i in range(1, n+1):
    cnt = 0
    visited = [False] * (n + 1)
    visited[i] = True
    q = deque([i])

    while q:
        v = q.popleft()

        for j in graph[v]:
            if not visited[j]:
                q.append(j)
                visited[j] = True
                cnt += 1

    if ans_max < cnt:
        ans_max = cnt
        ans.clear()
        ans.append(i)
    elif ans_max == cnt:
        ans.append(i)

print(*ans)