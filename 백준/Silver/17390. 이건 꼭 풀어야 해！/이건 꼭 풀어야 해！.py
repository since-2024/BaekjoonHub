import sys
input = sys.stdin.readline

n, q = map(int, input().split())

gp = [0] + list(map(int, input().split()))
gp.sort()

for i in range(2, n+1):
    gp[i] += gp[i-1]

for _ in range(q):
    l, r = map(int, input().split())
    print(gp[r] - gp[l-1])