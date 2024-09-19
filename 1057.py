import sys
input = sys.stdin.readline
from collections import deque

def get_parents(queue):
    global cnt
    tmp = deque()
    cnt += 1
    while len(queue) >= 2:
        node_1 = queue.popleft()
        node_2 = queue.popleft()
        if node_1 and node_2:
            print(cnt)
            exit()
        elif node_1 or node_2:
            tmp.append(1)
        else:
            tmp.append(0)

    if len(queue) == 1:
        node_1 = queue.popleft()
        if node_1:
            tmp.append(1)
        else:
            tmp.append(0)

    if len(tmp) == 1:
        print(cnt)
        exit()
    return tmp

N, A, B = map(int, input().split())
arr = [0 for _ in range(N)]
arr[A-1] = 1
arr[B-1] = 1
cnt = 0
queue = deque(arr)
while queue:
    queue = get_parents(queue)

print(-1)
