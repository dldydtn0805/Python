import sys
from collections import deque

# sys.stdin = open('input.txt')

def bfs():
    while queue:
        k, i, j = queue.popleft()
        for dk, di, dj in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
            nk, ni, nj = k + dk, i + di, j + dj
            if 0 <= nk < H and 0<= ni < N and 0<= nj < M:
                if not graph[nk][ni][nj]:
                    graph[nk][ni][nj] = graph[k][i][j] + 1
                    queue.append((nk,ni,nj))


M, N, H = map(int, input().split())

graph = [[[0]*M for _ in range(N)] for _ in range(H)]

queue = deque()
for h in range(H):
    for n in range(N):
        temp = list(map(int, input().split()))
        for m in range(M):
            if temp[m] == 1:
                graph[h][n][m] = 1
                queue.append((h,n,m))
            elif temp[m] == -1:
                graph[h][n][m] = -1

ans = 0
max_v = 0
bfs()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 0:
                ans = -1
                print(ans)
                exit()
            elif graph[h][n][m] > ans:
                ans = graph[h][n][m]
print(ans-1)