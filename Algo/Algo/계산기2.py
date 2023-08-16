import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    numbers = input()
    stack = []
    susik = ''
    # 곱셉이 덧셈보다 우선순위가 높다
    icp = {'*':2, '+':1}
    for num in numbers:
        if num not in '+,*':
            susik += num
        else:
            # 토큰 우선순위가 높다면 스택에 바로 넣기
            if len(stack) == 0 or icp[stack[-1]] < icp[num]:
                stack.append(num)
            else:
            # 토큰 우선순위가 낮거나 같다면 스택 탑에 있는게 우선순위가 더 크거나 같을때까지 수식에 넣기
                while stack and icp[stack[-1]] >= icp[num]:
                    susik += stack.pop()
                # 그 후에 스택에 넣기
                stack.append(num)
    # 잔여 연산자 수식에 넣기
    while stack:
        susik += stack.pop()
    stack = []

    for su in susik:
        if su not in '+,*':
            stack.append(int(su))
        else:
            # 계산 값 스택에 넣기
            if len(stack) > 1:
                b = stack.pop()
                a = stack.pop()
                if su == '+':
                    stack.append(a+b)
                else:
                    stack.append(a*b)
    print(f'#{tc}', stack[-1])

