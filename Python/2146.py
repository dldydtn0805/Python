import sys
input = sys.stdin.readline
from collections import deque
def bfs(si, sj):
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = -1
    tmp = []
    tmp.append((si, sj))
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N:
                if not visited[ni][nj]:
                    if arr[ni][nj] == 1:
                        queue.append((ni, nj))
                        tmp.append((ni, nj))
                        visited[ni][nj] = -1
    queue = deque()
    distance = [[0 for _ in range(N)] for _ in range(N)]
    for ti, tj in tmp:
        queue.append((ti, tj))
        distance[ti][tj] = 1
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N:
                if not distance[ni][nj]:
                    if not visited[ni][nj]:
                        if arr[ni][nj] == 1:
                            return distance[ci][cj] + 1
                        queue.append((ni, nj))
                        distance[ni][nj] = distance[ci][cj] + 1
    return 1e9
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 1e9
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j]:
            ans = min(ans, bfs(i, j))
print(ans-2)
