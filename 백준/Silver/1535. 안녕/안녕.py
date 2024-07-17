import sys
input = sys.stdin.readline

n = int(input())
dmg = [0] + list(map(int, input().split()))
joy = [0] + list(map(int, input().split()))

dp = [[0] * 100 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 100):
        if dmg[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-dmg[i]] + joy[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][-1])