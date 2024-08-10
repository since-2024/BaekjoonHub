import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

dp = a[:]
dm = a[:]

for i in range(n-1):
    a = list(map(int, input().split()))

    dp = [a[0] + max(dp[0], dp[1]), a[1] + max(dp), a[2] + max(dp[1], dp[2])]
    dm = [a[0] + min(dm[0], dm[1]), a[1] + min(dm), a[2] + min(dm[1], dm[2])]

print(max(dp), min(dm))