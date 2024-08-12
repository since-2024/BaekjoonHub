import sys
input = sys.stdin.readline

while True:
	n, m = input().split()
	n, m = int(n), int(float(m) * 100 + 0.05)
	
	if n == 0 and m == 0:
		break
	
	dp = [0] * (m+1)
	
	for _ in range(n):
		c, p = input().split()
		c, p = int(c), int(float(p) * 100 + 0.05)
		
		for i in range(p, m+1):
			dp[i] = max(dp[i], dp[i-p] + c)
	
	print(dp[-1])