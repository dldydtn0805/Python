import sys
# sys.stdin = open('input.txt')

while True:
    strings = list(input())
    if len(strings) == 1 and strings[0] == '.':
        break
    stack = []
    flag = 1
    for s in strings:
        if not stack:
            if s == '(' or s == '[':
                stack.append(s)
            elif s == ')' or s == ']':
                flag = 0
        else:
            if s == '(':
                stack.append(s)
            elif s == '[':
                stack.append(s)
            elif s == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    flag = 0
            elif s == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    flag = 0
    if stack:
        flag = 0
    if flag:
        print('yes')
    else:
        print('no')