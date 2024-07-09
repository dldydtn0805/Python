import sys
from collections import deque
# sys.stdin = open('input.txt')

def bfs(si, sj):
    queue = deque()
    queue.append((si,sj))
    while queue:
        ci, cj = queue.popleft()
        if ci == ti and cj == tj:
            print(graph[ci][cj]-1)
            return
        for di, dj in [[-2,-1],[-1,-2],[-2,1],[-1,2],[1,-2],[2,-1],[2,1],[1,2]]:
            ni, nj = ci + di, cj + dj
            if 0<=ni<I and 0<=nj<I:
                if graph[ni][nj] != 0:
                    continue
                queue.append((ni,nj))
                graph[ni][nj] = graph[ci][cj] + 1
T = int(input())
for _ in range(T):
    I = int(input())
    si, sj = map(int, input().split())
    ti, tj = map(int, input().split())
    graph = [[0]*I for _ in range(I)]
    graph[si][sj] = 1
    bfs(si,sj)
