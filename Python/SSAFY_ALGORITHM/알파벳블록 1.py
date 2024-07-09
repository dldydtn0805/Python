import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
n = int(input())
stack = []
temp = []
for _ in range(n):
    x = list(input().split())
    if x[0] == '1':
        stack.append(x[1])
        temp.append(x[1])
    elif x[0] == '2':
        stack = [x[1]] + stack
        temp.append(x[1])
    if x[0] == '3' and len(stack)>0:
        stack.remove(temp.pop())
if stack:
    result = ''
    while len(stack) >0:
        result += stack.pop()
    print(result[::-1])
else:
    print(0)