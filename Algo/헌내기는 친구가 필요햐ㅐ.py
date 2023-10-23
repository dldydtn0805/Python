# import sys; sys.stdin = open('input.txt')
from collections import deque
def bfs(i,j):
    cnt = 0
    queue = deque()
    queue.append((i,j))
    visited = [[0]*m for _ in range(n)]
    visited[i][j] = 1
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = ci + di, cj + dj
            if 0<=ni < n and 0<=nj < m:
                if not visited[ni][nj] and graph[ni][nj] != 'X':
                    if graph[ni][nj] == 'P':
                        cnt += 1
                    queue.append((ni,nj))
                    visited[ni][nj] = 1
    if cnt == 0:
        return 'TT'
    return cnt
n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            print(bfs(i,j))
            exit()
