import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while queue:
        ci, cj = queue.popleft()
        cnt = 0
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<R and 0<=nj<C:
                if arr[ni][nj] == 'X':
                    cnt += 1
        if cnt <= 1:
            ans.append((ci, cj))
R,C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
queue = deque()
ans = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'X':
            queue.append((i, j))
bfs()
for ai, aj in ans:
    arr[ai][aj] = '.'
for i in range(C):
    flag = True
    for j in range(R):
        if arr[j][i] == 'X':
            flag = False
            break
    if flag:
        for j in range(R):
            arr[j][i] = '-'
    if not flag:
        break
for i in range(C-1, -1, -1):
    flag = True
    for j in range(R):
        if arr[j][i] == 'X':
            flag = False
            break
    if flag:
        for j in range(R):
            arr[j][i] = '-'
    if not flag:
        break
for i in range(R):
    flag = True
    for j in range(C):
        if arr[i][j] == 'X':
            flag = False
            break
    if flag:
        for j in range(C):
            arr[i][j] = '-'
    if not flag:
        break
for i in range(R-1,-1,-1):
    flag = True
    for j in range(C):
        if arr[i][j] == 'X':
            flag = False
            break
    if flag:
        for j in range(C):
            arr[i][j] = '-'
    if not flag:
        break
for i in range(R):
    flag = True
    for j in range(C):
        if arr[i][j] != '-':
            print(arr[i][j], end='')
            flag = False
    if not flag:
        print()
