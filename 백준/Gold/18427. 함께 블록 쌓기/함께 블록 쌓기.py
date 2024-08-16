import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())

dp = [0] * (h+1)

for _ in range(n):
    blocks = list(map(int, input().split()))

    for i in range(h, 0, -1):
        if not dp[i]:
            continue

        for k in blocks:
            if i + k <= h:
                dp[i+k] += dp[i]

    for k in blocks:
        dp[k] += 1

print(dp[h] % 10007)