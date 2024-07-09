import sys
from collections import deque

# sys.stdin = open('input.txt')

def bfs():
    while queue:
        i, j = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = i + di, j + dj
            if 0<= ni < N and 0<= nj < M:
                if not graph[ni][nj]:
                    graph[ni][nj] = graph[i][j] + 1
                    queue.append((ni,nj))


M, N, = map(int, input().split())

graph = [[0]*M for _ in range(N)]

queue = deque()

for n in range(N):
    temp = list(map(int, input().split()))
    for m in range(M):
        if temp[m] == 1:
            graph[n][m] = 1
            queue.append((n,m))
        elif temp[m] == -1:
            graph[n][m] = -1

ans = 0
max_v = 0
bfs()

for n in range(N):
    for m in range(M):
        if graph[n][m] == 0:
            ans = -1
            print(ans)
            exit()
        elif graph[n][m] > ans:
            ans = graph[n][m]
print(ans-1)