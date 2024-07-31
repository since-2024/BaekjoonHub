import sys
input = sys.stdin.readline

n = int(input())

s = list(map(int, input().split()))
s.sort()

ans = 0

for i in s:
    if ans + 1 < i:
        break
    ans += i

print(ans + 1)