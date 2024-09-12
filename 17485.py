import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

directions = [
    [-1, -1],
    [-1, 0],
    [-1, 1]
]
dp = [[[1e9, 1e9, 1e9] for _ in range(M)] for _ in range(N)]
dp[0] = [[arr[0][i], arr[0][i], arr[0][i]] for i in range(M)]
for i in range(1, len(arr)):
    for j in range(M):
        for k in range(len(directions)):
            di, dj = directions[k]
            pi, pj = i + di, j + dj
            if 0<= pj< M:
                for l in range(len(dp[pi][pj])):
                    if l != k:
                        dp[i][j][k] = min(dp[i][j][k], dp[pi][pj][l] + arr[i][j])

res = 1e9
for ans in dp[-1]:
    for answer in ans:
        res = min(res, answer)
print(res)
