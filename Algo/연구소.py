# import sys; sys.stdin = open('input.txt')
from collections import deque

def bfs(queue, visited):
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0<=nj < m:
                if graph[ni][nj] == 0:
                    if not visited[ni][nj]:
                        visited[ni][nj] = 1
                        queue.append((ni,nj))

def make_star(cnt):
    global max_v
    if cnt == 3:
        queue = deque()
        visited = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 2:
                    queue.append((i,j))
                elif graph[i][j] == 1:
                    visited[i][j] = -1
        bfs(queue, visited)
        value = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0:
                    if graph[i][j] == 0:
                        value += 1

        if max_v < value:
            max_v = value
        return


    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_star(cnt+1)
                graph[i][j] = 0

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
max_v = 0
make_star(0)
print(max_v)