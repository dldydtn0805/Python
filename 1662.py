import sys
input = sys.stdin.readline

arr = list(input().rstrip())
stack = []
for i in range(len(arr)):
    cur = arr[i]
    if cur == ')':
        memo = 0
        while stack[-1] != '(':
            back = stack.pop()
            if back.isnumeric():
                memo += 1
            else:
                memo += int(back[1:])
        else:
            stack.pop()
            repeat = stack.pop()
            res = 0
            stack.append(f'!{int(repeat)*memo}')
    else:
        stack.append(cur)
ans = 0
for s in stack:
    if s.isnumeric():
        ans += 1
    else:
        ans += int(s[1:])
print(ans)

