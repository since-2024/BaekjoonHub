import sys
input = sys.stdin.readline

n, k = map(int, input().split())
study = [[]] + [list(map(int, input().split())) for _ in range(k)]

dp = [[0] * (n+1) for _ in range(k+1)]

for i in range(1, k+1):
    m, t = study[i]
    
    for j in range(1, n+1):
        if j >= t:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-t] + m)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[k][n])