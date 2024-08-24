n, k, l = map(int, input().split())

ans = 0
while k != l:
	k -= k//2
	l -= l//2
	ans += 1

print(ans)