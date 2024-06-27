import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = max(dp[i-1], dp[i])
    t, p = map(int, input().split())
    d_day = i + t - 1

    if d_day < n+1:
        dp[d_day] = max(dp[d_day], dp[i-1] + p)

print(dp[-1])