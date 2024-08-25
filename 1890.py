import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = []
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if dp[i][j] and graph[i][j]:
            weight = graph[i][j]
            for di, dj in [[1,0], [0,1]]:
                ni, nj = i+di*weight, j+dj*weight
                if 0<=ni<N and 0<=nj<N:
                    if not dp[ni][nj]:
                        dp[ni][nj] = dp[i][j]
                    else:
                        dp[ni][nj] += dp[i][j]
print(dp[-1][-1])
