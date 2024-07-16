import sys
input = sys.stdin.readline

def cal(n):
  global stack
  v = 0
  tmp = 0
  ret = False
  
  while stack:
    v = stack.pop()
    if str(v).isdigit():
      tmp += v
    else:
      if tmp == 0:
        tmp = 1
      break
    
  if n == ')' and v == '(':
    stack.append(2 * tmp)
    ret = True
  elif n == ']' and v == '[':
    stack.append(3 * tmp)
    ret = True
  
  return ret


s = input().rstrip()

stack = []

for i in s:
  if i == '(':
    stack.append(i)
  elif i == '[':
    stack.append(i)
  else:
    if not stack or not cal(i):
      stack = [0]
      break

ans = 0
for i in stack:
  if str(i).isdigit():
    ans += i
  else:
    ans = 0
    break
    
print(ans)