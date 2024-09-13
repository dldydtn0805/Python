import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    lst = list(input().rstrip().split())
    for elem in lst:
        arr.append(elem)
stack = []
sorted_arr = sorted(arr, key= lambda x : (x[0], int(x[2:])), reverse=True)
for elem in arr:
    if elem == sorted_arr[-1]:
        sorted_arr.pop()
    else:
        while stack and stack[-1] == sorted_arr[-1]:
            stack.pop()
            sorted_arr.pop()
        else:
            stack.append(elem)

if stack == sorted_arr:
    print('GOOD')
else:
    print('BAD')

