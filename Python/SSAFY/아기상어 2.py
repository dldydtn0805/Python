from collections import deque
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
def bfs():
    while queue:
        a, b = queue.popleft()
        for di, dj in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
            ni, nj = di + a, dj+b
            if 0<=ni<n and 0<=nj<m:
                if visited[ni][nj] == -1:
                    queue.append((ni,nj))
                    visited[ni][nj] = visited[a][b] + 1


n, m = map(int, input().split())
queue = deque()
visited = [[-1]*m for _ in range(n)]
for i in range(n):
    temp = list(input().split())
    for j in range(m):
        if temp[j] == '1':
            queue.append((i, j))
            visited[i][j] = 0

bfs()
max_v = 0
for i in range(n):
    for j in range(m):
        if max_v < visited[i][j]:
            max_v = visited[i][j]
print(max_v)

