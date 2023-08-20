import sys
sys.stdin = open('input.txt')

words = list(input())
susik = ''
stack = []
icp = {'+':1, '-':1, '*':2, '/':2, '(':3}
isp = {'+':1, '-':1, '*':2, '/':2, '(':0}

for word in words:
    # 숫자라면 수식에 넣고
    if word not in '(+-*/)':
        susik += word
    # 닫는 괄호라면 여는 괄호가 나올때까지 스택에서 꺼내서 수식에 넣고
    elif word == ')':
        while stack[-1] != '(':
            susik += stack.pop()
        stack.pop()
    # 여는괄호 혹은 계산 부호라면 수행한다 다음을
    else:
        # 스택이 비었거나 현재 토큰의 우선 순위가 높거나 같다면 그냥 스택에 넣기
        if not stack or isp[stack[-1]] < icp[word]:
            stack.append(word)
        # 현재 토큰의 우선 순위가 작거나 같다면
        elif isp[stack[-1]] >= icp[word]:
            # 스택이 있는 동안 수식에 스택을 팝해서 넣고
            while stack and isp[stack[-1]] >= icp[word]:
                susik += stack.pop()
            # 그 후에 스택에 넣기
            stack.append(word)
while stack:
    susik += stack.pop()
print(susik)
