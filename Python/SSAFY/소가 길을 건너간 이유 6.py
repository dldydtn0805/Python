from collections import deque
import sys
sys. stdin = open('input.txt')

def bfs(si, sj):
    visited[si][sj] = 1
    queue = deque()
    queue.append((si,sj))
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = ci + di, cj + dj
            if (ci, cj, ni, nj) in roads:
                continue
            if 0<=ni<n and 0<=nj<n:
                if visited[ni][nj] == 0:
                    if ni == ei and nj == ej:
                        return True
                    visited[ni][nj] = visited[ci][cj] + 1
                    queue.append((ni,nj))


n, k, r = map(int, input().split())
graph = [[0]*n for _ in range(n)]
# 길..
roads = set()
cows = []

for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    # 양방향으로 길을 담아줬어
    roads.add((r1 - 1, c1 - 1, r2 - 1, c2 - 1))
    roads.add((r2 - 1, c2 - 1, r1 - 1, c1 - 1))

# 소들을 담아줬어
for _ in range(k):
    x, y = map(int, input().split())
    cows.append(((x-1),(y-1)))

cnt = 0

print(cows)
# 2중포문 돌면서 bfs 해줬어
for i in range(len(cows)):
    si, sj = cows[i]
    visited = [[0]*n for _ in range(n)]
    if not bfs(si,sj):
        cnt += 1
print(cnt)

