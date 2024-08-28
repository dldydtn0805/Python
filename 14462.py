import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * (N + 1)
brr = [0] * (N + 1)
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    arr[i] = int(input())

for i in range(1, N + 1):
    brr[i] = int(input())

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if abs(arr[i] - brr[j]) <= 4:
            dp[i][j] = dp[i-1][j-1] + 1

print(dp[N][N])
