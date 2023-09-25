import sys
from collections import deque
# sys.stdin = open('input.txt')

def bfs(si,sj):
    queue = deque()
    queue.append((si,sj))
    while queue:
        ci, cj = queue.popleft()
        if ci == r2 and cj == c2:
            print(graph[ci][cj]-1)
            exit()
        for di, dj in [[-2,-1],[-2,1],[0,-2],[0,2],[2,-1],[2,1]]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<n:
                if graph[ni][nj] != 0:
                    continue
                queue.append((ni,nj))
                graph[ni][nj] = graph[ci][cj] + 1
    print(-1)
    exit()
    pass
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
graph = [[0]*n for _ in range(n)]
graph[r1][c1] = 1
bfs(r1, c1)



