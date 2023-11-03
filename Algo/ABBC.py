import sys
from collections import deque
# sys.stdin = open ('input.txt')
arr = list(input())
queue = deque()
result = []
cnt = 0

for i in range(len(arr)):
    if arr[i] == 'B':
        queue.append(i)
    elif arr[i] == 'C':
        if queue:
            arr[queue.popleft()] = '!@#$'
            cnt += 1

queue2 = deque()
for i in range(len(arr)):
    if arr[i] == 'A':
        queue2.append(i)
    elif arr[i] == 'B':
        if queue2:
            arr[queue2.popleft()] = '******'
            cnt += 1

print(cnt)