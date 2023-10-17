import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(si, sj):
    if visited[si][sj]:
        return
    queue = deque()
    queue.append((si,sj))
    visited[si][sj] = 1
    while queue:
        i, j = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = i+di , j+dj
            if visited[ni][nj]:

n = int(input())
arr = [list(input()) for _ in range(n)]

print(arr)
visited = [[0]*n for _ in range(n)]


