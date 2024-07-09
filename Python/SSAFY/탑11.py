import sys
# sys.stdin = open('input.txt')

N = int(input())
arr =list(map(int, input().split()))

arr = [0] + arr

result = [0 for _ in range(N+1)]
result[0] = 0
result[1] = 0

stack = [(0,0)]
for i in range(1, N+1):
    while stack:
        # print(stack)
        if stack[-1][0] < arr[i]:
            # print(f'stack {stack}')
            stack.pop()
        else:
            result[i] = stack[-1][1]
            # print(f'result {result}')
            break
    stack.append((arr[i], i))
    # print()

print(*result[1:])