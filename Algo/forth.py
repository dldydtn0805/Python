import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    susik = list(input().split())
    stack = []
    # 플래그 = 계산 가능
    flag = True
    for x in susik:
        if x in '.':
            # 계산 가능한 상태이고, 스택에 피연산자가 1개 보다 많이 남아있지 않아야함
            if flag and len(stack) == 1:
                print(f'#{tc}', stack[-1])
            else:
                print(f'#{tc}', 'error')
        elif x not in '+-/*':
            stack.append(int(x))
        else:
            # 계산하려면 스택에 피연산자가 1개보다 많아야 함
            if len(stack)>1:
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
            # 스택에 피연산자가 1개 이하라면 계산 불가
            else:
                flag = False
