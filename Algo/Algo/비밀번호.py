import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    a, b = input(). split()
    # 스택
    stack = []
    for i in b:
        # 스택의 탑과 현재 요소 비교
        if len(stack) > 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    X = ''
    for i in stack:
        X = X + i
    print(f'#{tc}', X)
