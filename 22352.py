import sys
from collections import deque
input = sys.stdin.readline

def bfs(si, sj):
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = after[si][sj]
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M:
                if not visited[ni][nj]:
                    if before[si][sj] == before[ni][nj]:
                        if after[si][sj] == after[ni][nj]:
                            queue.append((ni, nj))
                            visited[ni][nj] = after[ni][nj]
                        else:
                            queue.append((ni, nj))
                            visited[ni][nj] = -1

N, M = map(int, input().split())
before = [list(map(int, input().split())) for _ in range(N)]
after = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
flag = True
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if after[i][j] != before[i][j]:
                if flag:
                    bfs(i, j)
                    flag = False
                else:
                    print('NO'); exit()
            else:
                bfs(i, j)

for i in range(N):
    for j in range(M):
        if visited[i][j] != after[i][j]:
            print('NO'); exit()
print("YES")
