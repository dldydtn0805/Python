import sys
input = sys.stdin.readline
from collections import deque

def bfs(si, sj):
    queue = deque()
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue.append([si, sj])
    visited[si][sj] = 1
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M :
                if visited[ni][nj] == 0:
                    if arr[ni][nj] == 0:
                        queue.append([ni, nj])
                        visited[ni][nj] = visited[ci][cj] + 1
    return visited
N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

start = bfs(0, 0)
end = bfs(N-1, M-1)

ans = 1e9

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            flag_1 = 1e9
            flag_2 = 1e9
            for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    if start[ni][nj] != 0:
                        flag_1 = min(start[ni][nj], flag_1)
                    if end[ni][nj] != 0:
                        flag_2 = min(end[ni][nj], flag_2)
            if flag_1 != 1e9 and flag_2 != 1e9:
                ans = min(flag_1 + flag_2 + 1, ans)

if start[N-1][M-1]:
    ans = min(start[N-1][M-1], ans)

if ans != 1e9: print(ans)
else: print(-1)
