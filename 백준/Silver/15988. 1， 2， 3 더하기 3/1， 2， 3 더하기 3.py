n = int(input())
case = [int(input()) for _ in range(n)]
dp = [0] * 1000001

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, max(case)+1):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009

for i in case:
    print(dp[i])