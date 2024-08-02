from collections import defaultdict
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = defaultdict(list)

for _ in range(k):
    a, b, s = map(int, input().split())
    if a < b:
        graph[a].append([b, s])

dp = [[-1] * m for _ in range(n+1)]
dp[1][-1] = 0

for i in range(1, n):
    for j in range(1, m):
        if dp[i][j] == -1:
            continue
        for n, c in graph[i]:
            dp[n][j-1] = max(dp[n][j-1], dp[i][j] + c)

print(max(dp[-1]))