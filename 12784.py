import sys
sys.setrecursionlimit(10**6)

def dfs(sw, si):
    visited[si] = 1
    value = 0
    for nw, ni in adj_list[si]:
        if not visited[ni]:
            value += dfs(nw, ni)
            visited[ni] = 0
    if not value:
        return sw
    else:
        return min(value, sw)

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B, W = list(map(int, input().split()))
        adj_list[A].append([W, B])
        adj_list[B].append([W, A])
    visited = [0 for _ in range(N+1)]
    if N == 1:
        print(0)
    else:
        print(dfs(1e9, 1))
