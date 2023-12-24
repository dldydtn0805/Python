import sys
input = sys.stdin.readline
"""
선언된 숫자가 0인 경우에, 스택이 비어있지 않으면 스택을 하나 팝 해주고

0이 아니라면 스택에 넣어준다
"""
K = int(input())
stack = []
for _ in range(K):
    number = int(input())

    if number == 0:
        if len(stack)>0:
            stack.pop()
    else:
        stack.append(number)

print(sum(stack))