import sys
input = sys.stdin.readline

n, t = map(int, input().split())

arr = sorted(list(map(int, input().split())))

ans = 0

for i in range(n-2):
	for j in range(i+1, n-1):
		for k in range(j+1, n):
			tmp = arr[i] + arr[j] + arr[k]
			if tmp > t:
				continue
			else:
				ans = max(ans, tmp)

print(ans)