import sys
input = sys.stdin.readline

n, m = map(int, input().split())
day = [0]
page = [0]

for _ in range(m):
    d, p = map(int, input().split())
    day.append(d)
    page.append(p)

dp = [[0] * (n+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if j >= day[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-day[i]] + page[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[m][n])