from collections import deque
# import sys
# sys.stdin = open('input.txt')

n = int(input())

arr = deque(i for i in range(1,n+1))
while len(arr) > 1:
    x = arr.popleft()
    y = arr.popleft()
    arr.append(y)
print(arr[-1])