E, M, S = map(int, input().split())
E -= 1
M -= 1
S -= 1

for i in range(15 * 28 * 19+ 1):
	if i%15 == E and i%28 == M and i %19 == S:
		print(i+1)
		break