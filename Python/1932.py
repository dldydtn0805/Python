import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = arr[:]
for i in range(1, len(dp)):
    for j in range(len(dp[i])):
            try:
                if 0<=(j-1):
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dp[i][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j]
            except:
                dp[i][j] = dp[i-1][j-1] + dp[i][j]
print(max(dp[N-1]))
