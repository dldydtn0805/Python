import sys
input = sys.stdin.readline
from collections import deque

p, m = map(int, input().split())
queue = deque()
for _ in range(p):
    l, n = input().split()
    flag = True
    for i in range(len(queue)):
        if len(queue[i]) < m:
            if abs(int(queue[i][0][0])-int(l)) <= 10:
                queue[i].append((l, n))
                flag = False
                break
    if flag:
        queue.append([(l, n)])

for i in range(len(queue)):
    if len(queue[i]) == m:
        print('Started!')
    else:
        print('Waiting!')
    res = sorted(queue[i], key=lambda x:x[1])
    for j in range(len(res)):
        print(*res[j])
