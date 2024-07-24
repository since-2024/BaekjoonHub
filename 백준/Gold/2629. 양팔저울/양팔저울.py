from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))

w_max = max(w)

d = defaultdict(int)

for m in w:
    tmp = [m, -m]
    for k in d.keys():
        tmp.append(k-m)
        tmp.append(k+m)
    for i in tmp:
        d[i] = 1

_ = int(input())
qus = list(map(int, input().split()))
ans = []
for i in qus:
    if d[i]:
        ans.append('Y')
    else:
        ans.append('N')

print(*ans)