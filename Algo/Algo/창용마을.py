# import sys
from collections import deque
# sys.stdin = open('input.txt')
T = int(input())
def bfs(start):
    global cnt
    if visited[start]:
        return
    visited[start] = 1
    cnt += 1
    queue = deque()
    queue.append(start)
    while queue:
        cur = queue.popleft()
        for to in range(len(graph[cur])):
            next = graph[cur][to]
            if visited[next]:
                continue
            visited[next] = 1
            queue.append(next)

for tc in range(1, T+1):
    n, m = map(int, input().split())
    visited = [0]*(n)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        f, t = map(int, input().split())
        graph[f-1].append(t-1)
        graph[t-1].append(f-1)
    cnt = 0
    for i in range(n):
        bfs(i)
    print(f'#{tc}', cnt)
