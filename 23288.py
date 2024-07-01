import sys
input = sys.stdin.readline
from collections import deque


def move(direction, ci, cj):
    if direction == 'west':
        ni, nj = ci, cj - 1
        if 0 <= ni < N and 0 <= nj < M:
            next_i, next_j = ni, nj
        else:
            direction = 'east'
            next_i, next_j = ci, cj + 1
    elif direction == 'east':
        ni, nj = ci, cj + 1
        if 0 <= ni < N and 0 <= nj < M:
            next_i, next_j = ni, nj
        else:
            direction = 'west'
            next_i, next_j = ci, cj - 1
    elif direction == 'north':
        ni, nj = ci - 1, cj
        if 0 <= ni < N and 0 <= nj < M:
            next_i, next_j = ni, nj
        else:
            direction = 'south'
            next_i, next_j = ci + 1, cj
    elif direction == 'south':
        ni, nj = ci + 1, cj
        if 0 <= ni < N and 0 <= nj < M:
            next_i, next_j = ni, nj
        else:
            direction = 'north'
            next_i, next_j = ci - 1, cj

    return next_i, next_j, direction

def bfs(si, sj):
    queue = deque()
    queue.append((si, sj))
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[si][sj] = 1
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M:
                if not visited[ni][nj]:
                    if arr[si][sj] == arr[ni][nj]:
                        queue.append((ni, nj))
                        visited[ni][nj] = 1
    C = 0
    for i in range(len(visited)):
        C += visited[i].count(1)
    return C

def score(next_i, next_j):
    B = arr[next_i][next_j]
    C = bfs(next_i, next_j)
    return B*C

def roll(direction, cube):
    if direction == 'west':
        return [cube[2], cube[0], cube[5], cube[3], cube[4], cube[1]]
    elif direction == 'east':
        return [cube[1], cube[5], cube[0], cube[3], cube[4], cube[2]]
    elif direction == 'north':
        return [cube[4], cube[1], cube[2], cube[0], cube[5], cube[3]]
    elif direction == 'south':
        return [cube[3], cube[1], cube[2], cube[5], cube[0], cube[4]]

def rotate(direction, next_i, next_j, cube):
    A = cube[5]
    B = arr[next_i][next_j]
    if A > B:
        # 시계 방향 90도 회전
        if direction == 'west':
            direction = 'north'
        elif direction == 'east':
            direction = 'south'
        elif direction == 'north':
            direction = 'east'
        elif direction == 'south':
            direction = 'west'
    elif A < B:
        # 반시계 방향 90도 회전
        if direction == 'west':
            direction = 'south'
        elif direction == 'east':
            direction = 'north'
        elif direction == 'north':
            direction = 'west'
        elif direction == 'south':
            direction = 'east'

    return direction

# top, left, right, up, down, bottom
cube = [1, 4, 3, 2, 5, 6]
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ci, cj = 0, 0
direction = 'east'
ans = 0
for _ in range(K):
    next_i, next_j, direction = move(direction, ci, cj)
    cube = roll(direction, cube)
    ans += score(next_i, next_j)
    direction = rotate(direction, next_i, next_j, cube)
    ci, cj = next_i, next_j

print(ans)
