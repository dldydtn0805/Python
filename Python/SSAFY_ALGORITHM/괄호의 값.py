import sys
# sys.stdin = open('input.txt')

Str = input()
stack = []
if Str:
    for str in Str:
        stack.append(str)
        if len(stack) > 1 and stack[len(stack)-2] == '(' and stack[len(stack)-1] == ')':
            stack.pop()
            stack.pop()
            stack.append(2)
        if len(stack) > 1 and stack[len(stack) - 2] == '[' and stack[len(stack) - 1] == ']':
            stack.pop()
            stack.pop()
            stack.append(3)
        if len(stack) > 2 and stack[len(stack)-3] == '(' and stack[len(stack)-2] not in ['(',')','[',']']  and stack[len(stack)-1] == ')':
            stack.pop()
            temp = stack.pop()
            stack.pop()
            stack.append(2*temp)
        if len(stack) > 2 and stack[len(stack) - 3] == '[' and stack[len(stack) - 2] not in ['(',')','[',']'] and stack[len(stack) - 1] == ']':
            stack.pop()
            temp = stack.pop()
            stack.pop()
            stack.append(3*temp)
        if len(stack) > 1 and stack[len(stack) - 2] not in ['(',')','[',']'] and stack[len(stack) - 1] not in ['(',')','[',']']:
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
if len(stack) == 1 and stack[-1] not in ['(',')','[',']']:
    print(stack.pop())
else:
    print(0)
