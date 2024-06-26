import sys
input = sys.stdin.readline
from  collections import deque
def bfs(si, sj):
    if visited[si][sj] == -1:
        return False
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = -1
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M:
                if visited[ni][nj] == 1:
                    visited[ni][nj] = -1
                    queue.append((ni,nj))
    return True
N, M = map(int, input().split())
visited = [[0 for _ in range(M)] for _ in range(N)]
start = deque()
answer = 0
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(M):
        if arr[j] == 1:
            start.append((i, j))
            visited[i][j] = arr[j]
while start:
    si, sj = start.popleft()
    if bfs(si,sj):
        answer += 1
print(answer)
