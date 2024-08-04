from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

q = deque([i for i in range(1, n+1)])

ans = []
for _ in range(n):
    q.rotate(-k)
    ans.append(str(q.pop()))

print(f'<{", ".join(ans)}>')