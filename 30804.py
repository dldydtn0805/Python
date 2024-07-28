import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
arr = list(map(int, input().split()))

queue = deque()
cnt = 0
max_cnt = 0
for i in range(len(arr)):
    if queue:
        if len(queue) == 2:
            if queue[0][0] == arr[i]:
                queue.popleft()
                queue.append([arr[i], 0])
                cnt += 1
            elif queue[1][0] == arr[i]:
                queue[1][1] += 1
                cnt += 1
            else:
                queue.popleft()
                queue.append([arr[i], 0])
                cnt = 2 + queue[0][1]
        elif len(queue) == 1:
            if queue[0][0] == arr[i]:
                queue[0][1] += 1
                cnt += 1
            else:
                queue.append([arr[i], 0])
                cnt += 1
    else:
        queue.append([arr[i], 0])
        cnt += 1
    max_cnt = max(cnt, max_cnt)
print(max_cnt)
