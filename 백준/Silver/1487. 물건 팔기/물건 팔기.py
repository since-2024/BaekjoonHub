import sys
input = sys.stdin.readline

n = int(input())

arr = sorted([list(map(int, input().split())) for _ in range(n)])

ans = 0
max_total = 0
for a in arr:
    total = 0

    for j in range(n):
        if a[0] <= arr[j][0] and a[0] > arr[j][1]:
            total += a[0] - arr[j][1]

    if max_total < total:
        max_total = total
        ans = a[0]

print(ans)