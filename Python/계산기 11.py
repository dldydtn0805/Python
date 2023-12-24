import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    n = int(input())
    sentence = list(input())
    # print(sentence)
    stack = []
    susik = ''
    for x in sentence:
        if x not in '+':
            susik += x
            if len(stack)>0:
                susik += stack.pop()
        elif x == '+':
            stack.append(x)
    # print(susik)

    for x in susik:

        if x not in '+':
            stack.append(int(x))
        else:
            if len(stack)>1:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1+op2)
            else:
                break
    print(f'#{tc}', stack[-1])