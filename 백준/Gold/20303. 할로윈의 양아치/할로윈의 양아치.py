from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
candy = [0] + list(map(int, input().split()))

fr = [[] for _ in range(n + 1)]
gr = []
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    fr[a].append(b)
    fr[b].append(a)

q = deque()
for i in range(1, n+1):
    if visited[i]:
        continue

    visited[i] = True
    tmp, cnt = 0, 0
    q.append(i)

    while q:
        c = q.popleft()
        cnt += 1
        tmp += candy[c]

        for f in fr[c]:
            if not visited[f]:
                visited[f] = True
                q.append(f)

    gr.append([cnt, tmp])

dp = [0] * k

for i, c in gr:
    for j in range(k-1, i-1, -1):
        dp[j] = max(dp[j], dp[j-i] + c)

print(dp[-1])