import sys
input = sys.stdin.readline

case_1 = list(input().rstrip())
case_2 = list(input().rstrip())
N = len(case_1)
M = len(case_2)
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if case_1[i-1] == case_2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[N][M])

