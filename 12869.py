import sys
input = sys.stdin.readline
from collections import deque

def bfs(arr):
    queue = deque()
    if N == 3:
        visited[arr[0]][arr[1]][arr[2]] = 1
        queue.append((arr[0],arr[1],arr[2], 0))
    elif N == 2:
        visited[arr[0]][arr[1]][0] = 1
        queue.append((arr[0],arr[1],0, 0))
    elif N == 1:
        visited[arr[0]][0][0] = 1
        queue.append((arr[0], 0, 0, 0))
    while queue:
        ci, cj, ck, cnt = queue.popleft()
        for di, dj, dk in [[-9,-3,-1],[-9,-1,-3],[-3,-9,-1],[-3,-1,-9],[-1,-3,-9], [-1, -9, -3]]:
            ni, nj, nk = ci+di, cj+dj, ck+dk
            if 0<ni and 0<nj and 0<nk:
                if not visited[ni][nj][nk]:
                    queue.append((ni, nj, nk, cnt+1))
                    visited[ni][nj][nk] = 1
            elif 0<ni and 0<nj:
                if not visited[ni][nj][0]:
                    queue.append((ni, nj, 0, cnt+1))
                    visited[ni][nj][0] = 1
            elif 0<ni and 0<nk:
                if not visited[ni][0][nk]:
                    queue.append((ni, 0, nk, cnt+1))
                    visited[ni][0][nk] = 1
            elif 0<nj and 0<nk:
                if not visited[0][nj][nk]:
                    queue.append((0, nj,nk, cnt+1))
                    visited[0][ni][nk] = 1
            elif 0<ni:
                if not visited[ni][0][0]:
                    queue.append((ni, 0,0,cnt+1))
                    visited[ni][0][0] = 1
            elif 0<nj:
                if not visited[0][nj][0]:
                    queue.append((0,nj,0,cnt+1))
                    visited[0][nj][0]=1
            elif 0<nk:
                if not visited[0][0][nk]:
                    queue.append((0,0,nk,cnt+1))
                    visited[0][0][nk]=1
            else:
                print(cnt+1)
                exit()
N = int(input())
arr = list(map(int, input().split()))
visited = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]
bfs(arr)
