import sys
input = sys.stdin.readline
from  collections import deque

def apex(si, sj):
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1,1]]:
        ni, nj = si+di, sj+dj
        if 0<=ni<N and 0<=nj<M:
            if arr[ni][nj] > arr[si][sj]:
                return False
    return True

def bfs(si, sj):
    if visited[si][sj] != -1:
        return
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = arr[si][sj]
    current_visited = []
    current_visited.append((si, sj))
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1,1]]:
            ni, nj = ci+di, cj+dj
            if 0<= ni < N and 0<= nj < M:
                if visited[ni][nj] == -1:
                    if arr[ni][nj] == arr[ci][cj]:
                        visited[ni][nj] = arr[si][sj]
                        queue.append((ni, nj))
                        current_visited.append((ni, nj))
    while current_visited:
        ci, cj = current_visited.pop()
        if not apex(ci, cj):
            return False
    return True
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
visited = [[-1 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if bfs(i, j):
            answer += 1
print(answer)
