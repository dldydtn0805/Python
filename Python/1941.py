from itertools import combinations
from collections import deque

def bfs(si, sj):
    queue = deque()
    queue.append((si, sj))
    visited = [[0 for _ in range(5)] for _ in range(5)]
    visited[si][sj] = 1
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<5 and 0<=nj<5:
                if not visited[ni][nj]:
                    if (ni, nj) in case:
                        visited[ni][nj] = 1
                        queue.append((ni, nj))
    cnt = 0
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 1: cnt += 1
    if cnt == 7: return True
    else: return False
arr = [list(input()) for _ in range(5)]
ans = set()
total = []
for i in range(5):
    for j in range(5):
        total.append((i, j))
answer = 0
cases = (list(combinations(total, 7)))
for case in cases:
    cnt = 0
    for i in range(len(case)):
        ci, cj = case[i]
        if arr[ci][cj] == 'S':
            cnt += 1
    if cnt >= 4:
        si, sj = case[0]
        if bfs(si, sj): answer += 1
print(answer)
