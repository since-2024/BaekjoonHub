import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

ans = []
dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_dp = max(dp)
print(max_dp)

for i in range(n-1, -1, -1):
    if dp[i] == max_dp:
        ans.append(a[i])
        max_dp -= 1

ans.reverse()

print(*ans)