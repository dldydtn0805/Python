from collections import deque
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
queue = deque()
for _ in range(N):
    arr = list(map(int,input().split()))
    if arr[0] == 1:
        queue.insert(0, arr[1])
    elif arr[0] == 2:
        queue.append(arr[1])
    elif arr[0] == 3:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif arr[0] == 4:
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif arr[0] == 5:
        print(len(queue))
    elif arr[0] == 6:
        if queue:
            print(0)
        else:
            print(1)
    elif arr[0] == 7:
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)