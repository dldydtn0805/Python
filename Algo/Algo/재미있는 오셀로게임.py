import sys
sys.stdin = open('input.txt')

def bfs(i,j,color):
    visited[i][j] = color
    queue = []
    queue.append((i,j))
    di =[-1,-1,-1,1,1,1,0,0]
    dj =[0,1,-1,1,0,-1,-1,1]

    while queue:
        a, b = queue.pop(0)
        for k in range(8):
            for p in range(1,n+1):
                ni = a + di[k]*p
                nj = b + dj[k]*p
                if 0<=ni<n and 0<=nj<n:
                    print(ni, nj)
                    if visited[ni][nj] == -1:
                        break
                    else:
                        if visited[ni][nj] != color:
                            queue.append((ni,nj))
                        elif visited[ni][nj] == color:
                            while queue:
                                x, y = queue.pop(0)
                                visited[x][y] = color
                                # print(visited)
            # print(queue)
            while queue:
                x, y = queue.pop(0)
                visited[x][y] = color

T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    visited = [[-1] * (n) for _ in range(n)]
    visited[n//2-1][n//2-1] = 2
    visited[n//2-1][n//2] = 1
    visited[n//2][n//2-1] = 1
    visited[n//2][n//2] = 2

    for _ in range(m):
        i, j, color = map(int, input().split())
        bfs(i-1, j-1, color)

    a = 0
    b = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                a += 1
            if visited[i][j] == 2:
                b += 1

    print(visited)
    print(f'#{tc}', a, b)

