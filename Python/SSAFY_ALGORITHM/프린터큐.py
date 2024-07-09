import sys
from collections import deque
# sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = deque()
    for i in range(n):
        queue.append((arr[i], i))
    cnt = 0
    while queue:
        max_v = 0
        for i in range(len(queue)):
            if max_v < queue[i][0]:
                max_v = queue[i][0]
        if queue[0][0] == max_v:
            item = queue.popleft()
            cnt += 1
            if item[1] == m:
                print(cnt)
        else:
            queue.append(queue.popleft())