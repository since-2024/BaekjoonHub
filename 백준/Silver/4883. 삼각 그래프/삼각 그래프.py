import sys
input = sys.stdin.readline

cnt = 1

while 1:
    n = int(input())

    if n == 0:
        break

    k = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*3 for _ in range(n)]


    dp[1][0] = k[1][0] + k[0][1]
    dp[1][1] = k[1][1] + min(dp[1][0], k[0][1], k[0][1] + k[0][2])
    dp[1][2] = k[1][2] + min(dp[1][1], k[0][1], k[0][1] + k[0][2])

    for i in range(2, n):
        dp[i][0] = k[i][0] + min(dp[i-1][0], dp[i-1][1])
        dp[i][1] = k[i][1] + min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][0])
        dp[i][2] = k[i][2] + min(dp[i-1][1], dp[i-1][2], dp[i][1])

    print(f'{cnt}. {dp[n-1][1]}')
    cnt += 1