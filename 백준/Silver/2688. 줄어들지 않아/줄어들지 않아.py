import sys
input = sys.stdin.readline

t = int(input())
n_list = [int(input()) for _ in range(t)]

total = [0] * 65
total[0] = 1

n_max = max(n_list)
dp = [[0] * 10 for _ in range(n_max+1)]

for i in range(1, n_max+1):
    dp[i][0] = total[i-1]

    for j in range(1, 10):
        dp[i][j] = dp[i][j-1] - dp[i-1][j-1]

    total[i] = sum(dp[i])

for i in n_list:
    print(total[i])