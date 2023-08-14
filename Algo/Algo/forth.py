import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    susik = list(input().split())
    stack = []
    temp = len(stack)
    flag = 1
    for x in susik:
        if x in '.':
            break
        elif x not in '+-/*':
            stack.append(int(x))
        else:
            try:
                op2 = stack.pop()
                op1 = stack.pop()
                if x == '+':
                    stack.append(op1 + op2)
                elif x == '-':
                    stack.append(op1 - op2)
                elif x == '*':
                    stack.append(op1 * op2)
                elif x == '/':
                    stack.append(op1 // op2)
            except:
                pass

    if flag and len(stack)==1:
        print(f'#{tc}', stack.pop())
    else:
        print(f'#{tc}', 'error')