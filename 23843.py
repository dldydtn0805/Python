import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
queue = deque()
for i in range(N):
    if len(queue) < M:
        queue.append(arr[i])
    else:
        queue[queue.index(min(queue))] += arr[i]
print(max(queue))
