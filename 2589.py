import sys
input = sys.stdin.readline
from collections import deque

def bfs(si, sj):
    queue = deque()
    visited = [[0 for _ in range(W)] for _ in range(H)]
    queue.append([si, sj])
    visited[si][sj] = 1
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < H and 0 <= nj < W:
                if tres[ni][nj] == 'L':
                    if not visited[ni][nj]:
                        queue.append([ni,nj])
                        next_value = visited[ci][cj] + 1
                        visited[ni][nj] = next_value
                        if next_value > max_v[0]:
                            max_v[0] = next_value
                            max_idx[0], max_idx[1] = ni, nj


H, W = map(int, input().split())
tres = [list(input().rstrip()) for _ in range(H)]
max_v = [0]
max_idx = [0, 0]

for h in range(H):
    for w in range(W):
        if tres[h][w] == 'L':
            bfs(h, w)

max_v[0] -= 1

print(*max_v)
