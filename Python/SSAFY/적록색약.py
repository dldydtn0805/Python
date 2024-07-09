import sys
# sys.stdin = open('input.txt')

from collections import deque

def bfs(si, sj):
    global cnt
    if visited[si][sj]:
        return 0
    queue = deque()
    queue.append((si,sj))
    visited[si][sj] = 1
    while queue:
        i, j = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = i+di , j+dj
            if 0<= ni < n and 0<=nj < n:
                if not visited[ni][nj]:
                    if arr[i][j] == arr[ni][nj]:
                        visited[ni][nj] = 1
                        queue.append((ni,nj))
    cnt += 1

n = int(input())
arr = [list(input()) for _ in range(n)]


visited = [[0]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        bfs(i, j)

ans = []
ans.append(cnt)

cnt = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'




visited = [[0]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        bfs(i, j)

ans.append(cnt)

print(*ans)

