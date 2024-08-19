full_n = set(range(1, 10001))
d_n = set()

for i in range(1, 10001):
	for j in str(i):
		i += int(j)
	d_n.add(i)

ans = sorted(full_n - d_n)

for i in ans:
	print(i)