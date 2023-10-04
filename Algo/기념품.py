import sys
from collections import deque
# sys.stdin = open('input.txt')

n = int(input())
arr = deque(i for i in range(1, n+1))
i = 1
while len(arr)>1:
    arr.rotate(-(i**3-1))
    arr.popleft()
    i += 1
print(*arr)