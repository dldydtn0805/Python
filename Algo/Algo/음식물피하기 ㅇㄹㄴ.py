import sys
from collections import deque
sys.setrecursionlimit(10**9)

def dfs(i,j, cnt):
    global max_v
    visited[i][j] = 0
    if max_v < cnt:
        max_v = cnt
    for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
        ni, nj = i + di, j + dj
        if 0<=ni<n and 0<=nj<m:
            if visited[ni][nj] == 1:
                dfs(ni,nj,cnt+1)
                visited[ni][nj] = 1

input = sys.stdin.readline
n, m, k = map(int, input().split())
q = deque()
visited = [[0]*m for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    visited[a-1][b-1] = 1
    q.append((a-1,b-1))
max_v = 0
while q:
    i, j = q.pop()
    dfs(i,j,1)
print(max_v)