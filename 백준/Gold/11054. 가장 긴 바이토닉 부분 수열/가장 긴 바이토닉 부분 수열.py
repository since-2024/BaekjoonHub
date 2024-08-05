import sys
input = sys.stdin.readline

n = int(input())

s = list(map(int, input().split()))
r = s[::-1]

sa = [1] * n
ra = [1] * n

for i in range(n):
    for j in range(i):
        if s[i] > s[j]:
            sa[i] = max(sa[i], sa[j] + 1)
        if r[i] > r[j]:
            ra[i] = max(ra[i], ra[j] + 1)

ans = [0] * n
for i in range(n):
    ans[i] = sa[i] + ra[n-i-1] - 1

print(max(ans))