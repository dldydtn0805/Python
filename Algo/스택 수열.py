import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
result = [i for i in range(n, 0, -1)]
stack = []
answer = []
giho = []

while arr:
    if stack:
        if arr[-1] < stack[-1]:
            answer.append(stack.pop())
            giho.append('+')
        else:
            stack.append(arr.pop())
            giho.append('-')
    else:
        stack.append(arr.pop())
        giho.append('-')
while stack:
    answer.append(stack.pop())
    giho.append('+')
if answer == result:
    for i in range(len(giho)-1, -1, -1):
        print(giho[i])
else:
    print('NO')