import sys
input = sys.stdin.readline

c, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

max_cnt = c + max(data[x][1] for x in range(n)) + 1
dp = [1e9] * max_cnt
dp[0] = 0

for cost, per in data:
  for i in range(per, max_cnt):
    dp[i] = min(dp[i-per] + cost, dp[i])

print(min(dp[c:]))