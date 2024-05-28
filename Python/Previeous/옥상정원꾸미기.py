import sys
# sys.stdin = open('input.txt')

n = int(input())
buildings = [int(input())  for i in range(n)]
ans = 0
stack = []

for building in buildings:
    # 스택에 차례로
    while stack and stack[-1] <= building:
        stack.pop()
    stack.append(building)
    ans += len(stack) - 1

print(ans)