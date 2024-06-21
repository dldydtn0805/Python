import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def melt(si, sj):
    melted_cheeze = 0
    queue = deque()
    queue.append((si, sj))
    current_melting_cheeze = []
    current_turn = deepcopy(arr)
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M:
                if current_turn[ni][nj] == 0:
                    queue.append((ni, nj))
                    current_turn[ni][nj] = -1
                elif current_turn[ni][nj] == 1:
                    current_melting_cheeze.append((ni, nj))


    while current_melting_cheeze:
        mi, mj = current_melting_cheeze.pop()
        will_melt = 0
        if arr[mi][mj] == 1:
            for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
                ni, nj = mi+di, mj+dj
                if 0<=ni<N and 0<=nj<M:
                    if current_turn[ni][nj] == -1:
                        will_melt += 1
            if will_melt >= 2:
                melted_cheeze += 1
                arr[mi][mj] = 0
    return melted_cheeze

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().split())) for _ in range(N)]

total_cheeze = 0
si, sj = 0, 0
ans = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            total_cheeze += 1
        elif arr[i][j] == 0:
            si, sj = i, j

if total_cheeze == 0:
    print(0)
    exit()
else:
    while total_cheeze > 0:
        total_cheeze -= melt(si, sj)
        ans += 1
print(ans)
