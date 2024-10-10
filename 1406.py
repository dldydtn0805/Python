import sys
input = sys.stdin.readline
from collections import deque

arr = list(input().rstrip())
M = int(input())
N = len(arr)
idx = N
queue = deque(arr)
for tc in range(M):
    command = list(input().rstrip().split())
    # 커서를 왼쪽
    if command[0] == 'L':
        if idx > 0:
            queue.rotate(1)
            idx -= 1
    # 커서를 오른쪽
    elif command[0] == 'D':
        if idx < len(queue):
            queue.rotate(-1)
            idx += 1
    # 커서 왼쪽의 문자를 삭제
    elif command[0] == 'B':
        if idx > 0:
            idx -=1
            queue.pop()
    # 커서 왼쪽에 문자를 추가
    else:
        idx += 1
        queue.append(command[1])
queue.rotate(idx)
print(''.join(queue))
