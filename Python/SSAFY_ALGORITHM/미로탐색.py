from collections import deque
N, M = map(int, input().split())

visited = [[0]*M for _ in range(N)]

for i in range(N):
    temp = list(input())
    for j in range(M):
        if temp[j] == '0':
            visited[i][j] = -1

queue = deque()
queue.append((0,0))
visited[0][0] = 1
while queue:
    ci, cj = queue.popleft()
    for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
        ni, nj = ci+di, cj+dj
        if 0<=ni<N and 0<=nj<M:
            if visited[ni][nj] == 0:
                queue.append((ni,nj))
                visited[ni][nj] = visited[ci][cj] + 1
print(visited[N-1][M-1])
