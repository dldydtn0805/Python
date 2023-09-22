import sys
from collections import deque
# sys.stdin = open('input.txt')

def bfs(start):
    global cnt
    if not graph[start]:
        cnt += 1
        return
    if visited[start]:
        return
    cnt += 1
    visited[start] = 1
    queue = deque()
    queue.append((0, start))
    flag = [0] * (n + 1)
    flag[start] = 1
    flag2 = 0
    while queue:
        pre, cur = queue.popleft()
        for to in range(len(graph[cur])):
            next = graph[cur][to]
            if not visited[next]:
                visited[next] = 1
                queue.append((cur, next))
            if next != pre:
                if flag[next]:
                    flag2 = 1
            flag[next] = 1
    if flag2:
        cnt -= 1

tc = 0
while True:
    tc += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        f, t = map(int, input().split())
        graph[f].append(t)
        graph[t].append(f)
    cnt = 0
    visited = [0]*(n+1)

    for i in range(1,n+1):
        bfs(i)
    if cnt > 1:
        print(f'Case {tc}: A forest of {cnt} trees.')
    elif cnt == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: No trees.')
