def dfs(node):
    global cnt
    stack = []
    visited[node] = 0
    stack.append(node)
    while stack:
        cur = stack.pop()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = visited[cur] + 1
                if len(graph[next]) == 1:
                    cnt += visited[next]
                stack.append(next)

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
visited = [0] * (N+1)
dfs(1)
if cnt%2: print('Yes')
else: print('No')
