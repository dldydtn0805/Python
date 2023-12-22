import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
stack = []
for i in range(N):
    text = input().split()
    if len(text) == 2:
        stack.append(text[1])
    else:
        if text[0] == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif text[0] == 'size':
            print(len(stack))
        elif text[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif text[0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)

