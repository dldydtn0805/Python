import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int,input().split())
queue = deque(i for i in range(1, N+1))
print('<', end="")
while queue:
    queue.rotate(-(K-1))
    print(queue.popleft(), end='')
    if queue:
        print(',', end=" ")
print('>')
