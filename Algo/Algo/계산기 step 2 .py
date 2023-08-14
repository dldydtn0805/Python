"""
6528-*2/+
"""


stack = [0]*100
top = -1

susik = '6528-*2/+'

for x in susik:
    # 피연산자라면
    if x not in '+-/*':
        # push(x)
        top += 1
        stack[top] = int(x)
    else:
        op2 = stack[top]
        top -= 1
        op1 = stack[top]
        top -= 1
        # op1 + op2
        if x =='+':
            #pop()
            top += 1
            stack[top] = op1 + op2
        elif x =='-':
            top += 1
            stack[top] = op1 - op2
        elif x =='*':
            top += 1
            stack[top] = op1 * op2
        elif x =='/':
            top += 1
            stack[top] = op1 // op2
print(stack[top])
