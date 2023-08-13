import sys
sys.stdin = open('input.txt')

def dfs(a, b, V,adj_m):
    visited = [[0]*(V+1) for _ in range(V+1)]
    stack = []
    route = []
    visited[a][b] = 1
    for i in range(N):
        for j in range(M):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if visited[i][j] == 1:
                    visited[ni][nj] = 1
            while True:
                for x in range(1,V+1):
                    for y in range(1, V+1):
                        if adj_m[x][y] == 1 and visited[x][y] == 0:
                            stack.append(x,y)
                            visited[n] = 1
                            route.append(n)
                            break
                else:
                    if stack:
                        n = stack.pop()
                    else:
                        break

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    baechu = [[0]*(M) for _ in range(N)]
    adj_m = [[0] * (M) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for _ in range(K):
        x, y = map(int, input().split())
        baechu[y][x] = 1

    print(baechu)
    # dfs(0)