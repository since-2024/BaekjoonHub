n = int(input())
box = [0] + list(map(int, input().split()))
dp = [0] * 1001

for i in range(1, n+1):
    for j in range(i):
        if box[j] < box[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))