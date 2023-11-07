import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = deque(list(map(int, input().split())))
arr = deque()
for i in range(len(A)):
    if A[i] == 0:
        arr.append(B[i])

while C:
    cur = C.popleft()
    arr.appendleft(cur)
    print(arr.pop(), end=' ')
