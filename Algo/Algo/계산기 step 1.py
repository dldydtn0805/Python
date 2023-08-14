"""
(6+5*(2-8)/2)
6528-*2/+
"""


stack = [0]*100
top = -1
icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}

fx = '(6+5*(2-8)/2)'
susik = ''

# step 1
for x in fx:
    if x not in '(+-*/)': #피연산자
        susik += x
    elif x ==')': #'('까지 pop()
        while stack[top] != '(': #peek
            susik += stack[top]
            top -= 1
        top -= 1 #'(' 버림. pop
    else: #'(+-*/'
        if top==-1 or isp[stack[top]] < icp[x]: #토큰의 우선순위가 더 높으면
            top+=1
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top >-1 and isp[stack[top]] >=icp[x]:
                susik += stack[top]
                top -= 1
            top += 1 #push
            stack[top] = x

print(susik)

# step 2
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
