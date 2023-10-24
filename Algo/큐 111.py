import sys;
# sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque
queue = deque()
n = int(input())
for _ in range(n):
    temp = list(input().split())
    if temp[0] == 'push':
        queue.append(temp[1])
    elif temp[0] == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif temp[0] == 'back':
        if queue: print(queue[-1])
        else: print(-1)
    elif temp[0] == 'size':
        if queue: print(len(queue))
        else: print(0)
    elif temp[0] == 'empty':
        if not queue: print(1);
        else: print(0);
    elif temp[0] == 'pop':
        if queue: print(queue.popleft())
        else: print(-1)

