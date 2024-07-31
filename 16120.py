import sys
input = sys.stdin.readline

arr = list(input().rstrip())
stack = []
for i in range(len(arr)):
    stack.append(arr[i])
    if stack and len(stack) >= 4:
        if stack[-4:] == ['P', 'P', 'A', 'P']:
            stack[-4:] = ['P']

if stack and len(stack) >= 4:
    if stack[-4:] == ['P', 'P', 'A', 'P']:
        stack[-4:] = ['P']
if len(stack) == 1 and stack[0] == 'P':
    print('PPAP')
else:
    print('NP')
