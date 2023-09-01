import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
def dfs(x,y,cnt):
    global result, w_cnt
    visited[x][y] = 1

    if waterpark[x][y] == 'W':
        w_cnt -= 1
        total = cnt
        if total < result:
            result = total
        return

    if not w_cnt:
        return

    for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
        ni = x + di
        nj = y + dj
        if 0<=ni<n and 0<=nj<m and not visited[ni][nj]:
            dfs(ni,nj, cnt+1)
            visited[ni][nj] = 0

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    waterpark = [list(input()) for _ in range(n)]
    s = 0

    w_cnt = 0
    for i in range(n):
        for j in range(m):
            if waterpark[i][j] == 'W':
                w_cnt += 1

    for i in range(n):
        for j in range(m):
            result = 1e9
            visited = [[0]*m for _ in range(n)]
            if waterpark[i][j] == 'L':
                dfs(i,j,0)
                s += (result)
    print(f'#{tc}',s)