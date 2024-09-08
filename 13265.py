import sys
input = sys.stdin.readline
from collections import deque

def bfs(si):
    global flag
    if not visited[si]:
        queue = deque()
        queue.append(si)
        visited[si] = 1
        while queue:
            ci = queue.popleft()
            for ni in adj_list[ci]:
                if not visited[ni]:
                    queue.append(ni)
                    visited[ni] = 1 if visited[ci] == 2 else 2
                    for check in adj_list[ni]:
                        if visited[check]:
                            if visited[check] == visited[ni]:
                                flag = False
                                return

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    adj_list = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        adj_list[x].append(y)
        adj_list[y].append(x)
    flag = True
    visited = [0 for _ in range(n)]
    for i in range(n):
        bfs(i)
    if flag:
        print('possible')
    else:
        print('impossible')
