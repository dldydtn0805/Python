import sys
input = sys.stdin.readline
import heapq
from collections import deque

directions = [[-1,0],[0,1],[1,0],[0,-1]]

def move(cri, crj, cbi, cbj, di, dj, visited):
    red = True
    blue = True
    flag = False
    nri, nrj, nbi, nbj = cri, crj, cbi, cbj
    for _ in range(20):
        if red:
            nri, nrj = nri + di, nrj + dj
            if arr[nri][nrj] == 'O':
                flag = True
        if blue:
            nbi, nbj = nbi + di, nbj + dj
            if arr[nbi][nbj] == 'O':
                return cri, crj, cbi, cbj
        if arr[nri][nrj] == '#':
            nri, nrj = nri - di, nrj - dj
            red = False
        if arr[nbi][nbj] == '#':
            nbi, nbj = nbi - di, nbj - dj
            blue = False
        if nri == nbi and nrj == nbj:
            if red:
                nri, nrj = nri - di, nrj - dj
                red = False
            elif blue:
                nbi, nbj = nbi - di, nbj - dj
                blue = False
    if flag:
        if visited[cri][crj][cbi][cbj] + 1 <= 10:
            print(visited[cri][crj][cbi][cbj] + 1)
            exit()
    return nri, nrj, nbi, nbj

def bfs(ei, ej):
    queue = deque()
    queue.append((ri, rj, bi, bj))
    visited = [[[[-1 for _ in range(M)]for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[ri][rj][bi][bj] = 0
    while queue:
        cri,crj,cbi,cbj = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            nri, nrj, nbi,nbj = move(cri, crj, cbi, cbj, di, dj, visited)
            if visited[nri][nrj][nbi][nbj] == -1:
                queue.append((nri, nrj, nbi, nbj))
                visited[nri][nrj][nbi][nbj] = visited[cri][crj][cbi][cbj] + 1
    return visited[ei][ej]
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
ans = [1e9]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            ri, rj = i, j
        elif arr[i][j] == 'B':
            bi, bj = i, j
        elif arr[i][j] == 'O':
            ei, ej = i, j
bfs(ei, ej)
print(-1)
