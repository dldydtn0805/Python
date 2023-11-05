import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
queue = deque()
for _ in range(N):
    arr = list(input().split())
    if len(arr) > 1:
        queue.append(arr[1])
    else:
        if arr[0] == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif arr[0] == 'size':
            print(len(queue))
        elif arr[0] == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif arr[0] == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif arr[0] == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)


