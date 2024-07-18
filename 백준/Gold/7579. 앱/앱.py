import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mem = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
max_cost = sum(cost) + 1
dp = [[0] * max_cost for _ in range(n+1)]

for i in range(1, n + 1):
  for j in range(0, max_cost):
    if j >= cost[i]:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i]] + mem[i])
    else:
      dp[i][j] = dp[i-1][j]

for i, memory in enumerate(dp[n]):
  if memory >= m:
    print(i)
    break
