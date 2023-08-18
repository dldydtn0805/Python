import sys
sys.stdin = open('input.txt')


def bfs(si, sj):
    queue = []
    visited = [[0]*16 for _ in range(16)]
    visited[si][sj] = 1
    queue.append((si, sj))
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    while queue:
        si, sj = queue.pop(0)
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if 0<= ni<16 and 0<= nj <16:
                if visited[ni][nj] == 0 and miro[ni][nj] != 1:
                    queue.append((ni,nj))
                    visited[ni][nj] = 1

    return visited

for tc in range(1, 11):
    n = int(input())
    miro = [list(map(int,input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                si, sj = i, j
    for i in range(16):
        for j in range(16):
            if miro[i][j] ==3:
                gi, gj = i, j
    result = bfs(si, sj)

    if result[gi][gj]:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)
