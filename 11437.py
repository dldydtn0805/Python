import sys
input = sys.stdin.readline
from collections import deque

def bfs(si):
    queue = deque()
    queue.append(si)
    parent = [-1 for _ in range(N+1)]
    depth = [-1 for _ in range(N+1)]
    parent[si] = si
    depth[si] = 0
    while queue:
        cur = queue.popleft()
        for next in adj_list[cur]:
            if depth[next] == -1:
                queue.append(next)
                parent[next] = cur
                depth[next] = depth[cur] + 1
    return parent, depth

def find_lca(a, b, parent, depth):
    while depth[a] > depth[b]:
        a = parent[a]
    while depth[b] > depth[a]:
        b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

N = int(input())
adj_list = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)
M = int(input())
arr = [list(map(int, input().split())) for _ in range(M)]
parent, depth = bfs(1)
for A, B in arr:
    print(find_lca(A, B, parent, depth))
