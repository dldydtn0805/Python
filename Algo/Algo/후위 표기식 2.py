import sys
sys.stdin = open('input.txt')
stack = [0]*100
top = -1
icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}

fx = list(input())
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
        elif isp[stack[top]] >= icp[x]: #토큰의우선순위가 더 낮으면
            while top >-1 and isp[stack[top]] >=icp[x]:
                susik += stack[top] #pop
                top -= 1
            top += 1 #push
            stack[top] = x

print(susik)