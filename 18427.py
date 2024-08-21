import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, H = map(int, input().split())
arr = [[0] + list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(H+1)] for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(H+1):
        if dp[i][j]:
            for k in arr[i]:
                if j + k <= H:
                    dp[i+1][j+k] = (dp[i][j] + dp[i+1][j+k]) % 10007

print(dp[N][H])
