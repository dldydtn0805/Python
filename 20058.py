import sys
input = sys.stdin.readline
from collections import deque

def storm(level):
    new_ice = [[0 for _ in range(2**N)] for _ in range(2**N)]
    si, sj = 0, 0
    while si < 2**N and sj < 2**N:
        ei, ej = si + 2 ** level, sj + 2 ** level
        # 회전 하는 로직
        for i in range(si, ei):
            for j in range(sj, ej):
                new_ice[j-sj+si][ei-1-i+sj] = ice[i][j]
        # 다음 턴
        if sj + 2**level < 2**N:
            sj += 2**level
        else:
            if si + 2**level < 2**N:
                si += 2**level
                sj = 0
            else:
                break
    next_ice = fire(new_ice)
    return next_ice

def fire(cur_ice):
    melting_list = []
    for i in range(2**N):
        for j in range(2**N):
            if cur_ice[i][j]:
                cnt = 0
                for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
                    ni, nj = i+di, j+dj
                    if 0<=ni<2**N and 0<=nj<2**N:
                        if cur_ice[ni][nj]:
                            cnt += 1
                # 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸
                if cnt < 3:
                    melting_list.append([i, j])
    for mi, mj in melting_list:
        cur_ice[mi][mj] -= 1
    return cur_ice

def bfs(si, sj):
    queue = deque()
    queue.append([si, sj])
    visited[si][sj] = 1
    cnt = 1
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<2**N and 0<=nj<2**N:
                if not visited[ni][nj] and ice[ni][nj]:
                    queue.append([ni,nj])
                    visited[ni][nj] = 1
                    cnt += 1
    max_v[0] = max(max_v[0], cnt)

N, Q = map(int, input().split())
ice = [list(map(int,input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

for level in L:
    ice = storm(level)
max_v = [0]
visited = [[0 for _ in range(2**N)] for _ in range(2**N)]
total = 0
for i in range(2 ** N):
    total += sum(ice[i])

for i in range(2**N):
    for j in range(2**N):
        if not visited[i][j] and ice[i][j]:
            bfs(i, j)


print(total)
print(*max_v)
