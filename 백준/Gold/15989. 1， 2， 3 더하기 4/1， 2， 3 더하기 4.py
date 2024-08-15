import sys
input = sys.stdin.readline

t = int(input())

arr = [int(input()) for _ in range(t)]

max_cnt = max(arr) + 1

dp = [1] * max_cnt

for i in range(2, max_cnt):
    dp[i] += dp[i-2]

for i in range(3, max_cnt):
    dp[i] += dp[i-3]

for i in arr:
    print(dp[i])