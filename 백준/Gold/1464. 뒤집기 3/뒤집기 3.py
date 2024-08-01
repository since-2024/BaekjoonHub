import sys
input = sys.stdin.readline

s = list(input().rstrip())

t = s[0]
ans = [t]

for i in range(1, len(s)):
	if t < s[i]:
		ans.reverse()
		ans.append(s[i])
		ans.reverse()
	else:
		t = s[i]
		ans.append(t)

print(''.join(reversed(ans)))