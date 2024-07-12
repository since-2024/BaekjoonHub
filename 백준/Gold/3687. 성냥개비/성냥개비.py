import sys
input = sys.stdin.readline

t = int(input())
n_list = [int(input()) for _ in range(t)]
n_max = max(n_list)

# 2 3 4 5 6    7
# 1 7 4 2 6(0) 8
#
# 8   10   2+6
# 9   18   2+7
# 10  22   5+5
# 11  20   5+6
# 12  28   5+7
# 13  68   6+7
# 14  88   7+7
# 15  108  2+6+7

dp = [0, 0, 1, 7, 4, 2, 6, 8] + [float('inf')] * (101-8)

for i in range(8, n_max+1):
    for j in range(2, i-1):
        dp[i] = min(dp[i], int(str(dp[j]) + str(dp[i-j])))
        if j == 6:
            dp[i] = min(dp[i], int(str(dp[i-j]) + '0'))


def min_num(n):
    return dp[n]


def max_num(n):
    # 2 3 4  5  6   7   8
    # 1 7 11 71 111 711 1111

    digit = (n - 2) // 2
    f = '7' if n % 2 == 1 else '1'
    ret = [f] + ['1'] * digit

    return ''.join(ret)


for n in n_list:
    print(min_num(n), max_num(n))