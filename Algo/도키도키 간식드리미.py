import sys
# sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))

goal = 0
stack = []

for i in range(len(arr)):
    if arr[i] == goal + 1:
        goal += 1
    else:
        stack.append(arr[i])
    while stack and stack[-1] == goal + 1:
        stack.pop()
        goal += 1

# if stack:
#     print('Sad')
#     exit()

if goal == N:
    print('Nice')
else:
    print('Sad')