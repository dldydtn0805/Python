import sys
from collections import deque
input = sys.stdin.readline

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    next_turn = []
    while q:
        ci, cj = q.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni = ci+di
            nj = cj+dj
            if 0<=ni< N and 0<=nj<M:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append((ni,nj))
                    next_turn.append((ni,nj))
                elif visited[ni][nj] == -1:
                    next_turn.append((ni,nj))
                elif visited[ni][nj] == -2:
                    return True
    else:
        for nti, ntj in next_turn:
            visited[nti][ntj] = 0
        return False

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1
visited = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    arr = list(input())
    for j in range(len(arr)):
        if arr[j] == '1': visited[i][j] = -1
        elif arr[j] == '0': visited[i][j] = 0
        elif arr[j] == '*': visited[i][j] = 1
        elif arr[j] == '#': visited[i][j] = -2

cnt = 1
while not bfs(x1,y1):
    cnt += 1
print(cnt)
