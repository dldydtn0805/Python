import sys
input = sys.stdin.readline
def DFS(x, y, count):
    global answer
    answer = max(answer, count)
    visited[ord(보드[x][y])-65] = 1
    for di, dj in [[1,0], [-1,0], [0,1], [0,-1]]:
        nx = x + di
        ny = y + dj
        if 0<=nx<R and 0<=ny<C:
            if not visited[ord(보드[nx][ny])-65]:            
                DFS(nx, ny, count+1)
                visited[ord(보드[nx][ny])-65] = 0
R, C = map(int, input().rstrip().split())
보드 = [list(input().rstrip()) for _ in range(R)]
visited = [0]*26
answer = 0
DFS(0, 0, 1)
print(answer)
