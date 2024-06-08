# == solved with dictionary ==

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = list(input().rstrip())
    dic = dict()

    for i in s:
        if i != ' ':
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

    v_list = sorted(dic.values(), reverse=True)

    if v_list[0] == v_list[1]:
        print('?')
    else:
        print(max(dic, key=dic.get))
