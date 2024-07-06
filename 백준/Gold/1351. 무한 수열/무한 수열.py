from collections import defaultdict
import sys
input = sys.stdin.readline

n, p, q = map(int, input().split())

dp = defaultdict(int)
dp[0] = 1

def dfs(n):
  if dp[n] == 0:
    dp[n] = dfs(n//p) + dfs(n//q)
  
  return dp[n]

print(dfs(n))
