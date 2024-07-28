import sys
input = sys.stdin.readline
from collections import deque

def bfs(si, sj):
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = 1
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<H and 0<=nj<W:
                if arr[ni][nj] == '#':
                    if not visited[ni][nj]:
                        queue.append((ni, nj))
                        visited[ni][nj] = 1
T = int(input())
for _ in range(T):
    H, W = map(int, input().rstrip().split())
    arr = [list(input()) for _ in range(H)]
    visited = [[0 for _ in range(W)] for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j] and arr[i][j] == '#':
                cnt += 1
                bfs(i, j)
    print(cnt)
