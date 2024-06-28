import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	n = int(input())
	
	dp = [[] for _ in range(41)]
	
	dp[0] = [1, 0]
	dp[1] = [0, 1]
	
	for i in range(2,  n+1):
		a_0, a_1 = dp[i-2]
		b_0, b_1 = dp[i-1]
		dp[i] = [a_0+b_0, a_1+b_1]
		
	print(*dp[n])