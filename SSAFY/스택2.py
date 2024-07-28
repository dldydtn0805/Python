import sys
input = sys.stdin.readline
n = int(input())

stack = []

for _ in range(n):
    joy = list(input().rstrip().split())
    if joy[0] == '1':
        stack.append(joy[1])
    elif joy[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif joy[0] == '3':
        print(len(stack))
    elif joy[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
