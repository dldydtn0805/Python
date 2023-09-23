import sys
sys.stdin = open('input.txt')

# 후위 계산식 만들기
def inorder(k):
    global susik
    if k:
        inorder(c1[k])
        inorder(c2[k])
        susik += [value[k]]

T = 10
for tc in range(1, T + 1):
    n = int(input())
    # 왼쪽
    c1 = [0]*(n+1)
    # 오른쪽
    c2 = [0]*(n+1)
    value = [0] *(n+1)
    susik = []
    for _ in range(n):
        # 좌우노드 배열, 값 배열 구성
        word = list(input().split())
        index = int(word[0])
        if len(word) > 2:
            c1[index] = int(word[2])
            c2[index] = int(word[3])
        value[index] = word[1]
    # 후위 계산식 제작
    inorder(1)
    # 계산기
    stack = []
    for element in susik:
        if element not in ['-', '+', '*', '/']:
            stack.append(element)
        else:
            if len(stack)>1:
                b = int(stack.pop())
                a = int(stack.pop())
                if element == '*':
                    stack.append(a*b)
                if element == '/':
                    stack.append(a//b)
                if element == '+':
                    stack.append(a+b)
                if element == '-':
                    stack.append(a-b)
    print(f'#{tc}', *stack)