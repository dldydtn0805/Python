import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
from collections import deque
def bfs():
    while queue:
        a, b = queue.popleft()
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            if visited[ni][nj] != -1:
                continue
            queue.append((ni,nj))
            visited[ni][nj] = visited[a][b] + 1


T = int(input())
for tc in range(1, T+1):
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    n, m = map(int, input().split())
    s = 0
    visited = [[-1]*m for _ in range(n)]
    queue = deque()
    for i in range(n):
        tmp = input()
        for j in range(m):
            if tmp[j] == 'W':
                queue.append((i, j))
                visited[i][j] = 0

    bfs()
    for i in range(n):
        for j in range(m):
            s += visited[i][j]
    # print(visited)
    print(f'#{tc}',s)