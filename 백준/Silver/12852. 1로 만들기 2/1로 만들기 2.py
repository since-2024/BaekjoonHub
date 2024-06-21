n = int(input())

dp = [[0, 0] for _ in range(n+1)]

for i in range(2, n+1):
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = i-1

    tmp_2 = i // 2
    tmp_3 = i // 3

    if i % 2 == 0:
        if dp[i][0] > dp[tmp_2][0] + 1:
            dp[i][0] = dp[tmp_2][0] + 1
            dp[i][1] = tmp_2
    if i % 3 == 0:
        if dp[i][0] > dp[tmp_3][0] + 1:
            dp[i][0] = dp[tmp_3][0] + 1
            dp[i][1] = tmp_3

print(dp[n][0])

ans = []

idx = n
while idx != 0:
    ans.append(idx)
    idx = dp[idx][1]

print(*ans)