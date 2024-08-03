import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(si):
    visited[si] = [1, i]
    for ni in adjList[si]:
        if not visited[ni][0]:
            dfs(ni)
N, M = map(int,input().split())
adjList = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int,input().split())
    adjList[s].append(e)
    adjList[e].append(s)

visited = [[0, 0]for _ in range(N+1)]
cnt = 0
for i in range(1, N+1):
    if not visited[i][0]:
        dfs(i)
arr = list(map(int,input().split()))

for i in range(1, N):
    if visited[arr[i]][1] != visited[arr[i-1]][1]:
        cnt += 1
print(cnt)
