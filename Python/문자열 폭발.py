import sys
# sys.stdin = open('input.txt')

Str = input()
Boom = list(input())
stack = []
for str in Str:
    stack.append(str)
    if len(stack) >= len(Boom):
        if stack[len(stack)-len(Boom):len(stack)] == Boom:
            temp = len(Boom)
            while temp:
                stack.pop()
                temp -= 1
if stack:
    ans = ''.join(stack)
    print(ans)
else:
    print('FRULA')