import sys
sys.stdin = open('input.txt')

def bfs(si,sj, cnt, value):
    queue = []
    queue.append((si,sj))
    visited[si][sj] = arr[si][sj]
    cnt = 0
    while queue: # 재귀 필요
        if cnt == 4:
            cnt = 0
            continue
        i, j = queue.pop(0)
        if j % 2 :
            for di, dj in [[1,0], [0,1], [1,0], [0,-1], [1,1], [1,-1]]:
                ni = di + i
                nj = dj + j
                if 0<=ni<n and 0<=nj<m:
                    if not visited[ni][nj]:
                        visited[ni][nj] = visited[i][j] + arr[ni][nj]
                        cnt += 1
                    if visited[ni][nj] < visited[i][j] + arr[i][j]:
                        visited[ni][nj] = visited[i][j] + arr[ni][nj]
        else:
            for di, dj in [[1,0], [0,1], [1,0], [0,-1], [-1,1], [-1,-1]]:
                ni = di + i
                nj = dj + j
                if 0 <= ni < n and 0 <= nj < m:
                    if not visited[ni][nj]:
                        visited[ni][nj] = visited[i][j] + arr[ni][nj]
                        cnt += 1
                    if visited[ni][nj] < visited[i][j] + arr[i][j]:
                        visited[ni][nj] = visited[i][j] + arr[ni][nj]
T = int(input())
for tc in range(1, T + 1):
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            bfs(i,j)
    print(max(max(visited))**2)