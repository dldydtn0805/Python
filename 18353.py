import sys
input = sys.stdin.readline

N = int(input())
army = list(map(int, input().split()))
ans = 0
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = army[0]
for i in range(N):
    for j in range(i+1):
        cur = army[i]
        if i == 0 and j == 0:
            continue
        elif j == 0:
            dp[i][j] = max(dp[i-1][j], cur)
            continue
        dp[i][j] = dp[i-1][j]
        if cur < dp[i][j-1]:
            dp[i][j] = max(cur, dp[i][j])

for cnt in dp[-1]:
    if not cnt:
        ans += 1
print(ans)

