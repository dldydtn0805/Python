import sys
# sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    stack = []
    flag = 'YES'
    for i in range(len(arr)):
        if stack:
            if arr[i] == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    flag = 'NO'
            elif arr[i] == '(':
                stack.append(arr[i])
        else:
            stack.append(arr[i])
    if stack:
        flag = 'NO'
    print(flag)
