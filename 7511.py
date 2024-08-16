import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(si):
    if not visited[si]:
        visited[si] = tmp
        for ni in adj_list[si]:
            dfs(ni)

T = int(input())
for tc in range(T):
    n = int(input())
    k = int(input())
    adj_list = [[] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
    visited = [0 for _ in range(n)]
    tmp = 1
    for i in range(n):
        dfs(i)
        tmp += 1
    m = int(input())
    print(f'Scenario {tc+1}:')
    for _ in range(m):
        u, v = map(int, input().split())
        print(1 if visited[u] == visited[v] else 0)
    print()
