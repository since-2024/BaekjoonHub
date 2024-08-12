import sys
input = sys.stdin.readline

n = int(input())

balls = []
c = 0
k = 1

while c <= n:
	c += k * (k+1) // 2
	balls.append(c)
	k += 1

dp = [300001] * (n+1)

for i in range(1, n+1):
	for b in balls:
		if b == i:
			dp[i] = 1
			break
		
		if b > i:
			break
		
		dp[i] = min(dp[i], dp[i-b] + 1)

print(dp[n])