import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num = [0] + list(map(int, input().split()))

l = [list(map(int, input().split())) for _ in range(m)]

dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = dp[i-1] + num[i]

for a, b in l:
    print(dp[b] - dp[a-1])