import sys
input = sys.stdin.readline

for _ in range(3):
    t = int(input())

    c = [0] * t
    n = [0] * t
    target = 0

    for i in range(t):
        c[i], n[i] = map(int, input().split())

        target += c[i] * n[i]

    if target % 2 != 0:
        print(0)
        continue

    target //= 2

    dp = [1] + [0] * target

    for i in range(t):
        for k in range(target, c[i] - 1, -1):
            if dp[k - c[i]]:
                for j in range(n[i]):
                    if k + c[i] * j <= target:
                        dp[k + c[i] * j] = 1
    print(dp[target])