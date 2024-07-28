import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
T = int(input())
def f(x,y):
    global total
    visited[x][y] = 1
    total += 1
    for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
        ni = x + di
        nj = y + dj
        if 0<=ni<n and 0<=nj<n:
            if a[ni][nj] == a[x][y] + 1:
                visited[ni][nj] = visited[x][y] + 1
                f(ni,nj)

for tc in range(1, T+1):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    result = 0
    startroom = 1e9
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                total = 0
                f(i,j)
                if total > result:
                    result = total
                    startroom = a[i][j]
                elif total == result:
                    startroom = min(startroom, a[i][j])

    print(f'#{tc}', startroom, result)